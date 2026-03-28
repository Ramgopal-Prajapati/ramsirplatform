from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from django.http import JsonResponse
from django.utils import timezone
from django.db.models import Q
import json
import urllib.request
import urllib.error

from .models import (
    Course, Module, Enrollment, ModuleProgress,
    Payment, Event, Review, Category, UserProfile
)
from .forms import RegisterForm, ProfileUpdateForm, ReviewForm, PaymentForm


def home(request):
    featured_courses = Course.objects.filter(is_featured=True, is_active=True)[:6]
    free_courses = Course.objects.filter(course_type='free', is_active=True)[:4]
    paid_courses = Course.objects.filter(course_type='paid', is_active=True)[:4]
    upcoming_events = Event.objects.filter(is_active=True, event_date__gte=timezone.now())[:3]
    categories = Category.objects.all()

    context = {
        'featured_courses': featured_courses,
        'free_courses': free_courses,
        'paid_courses': paid_courses,
        'upcoming_events': upcoming_events,
        'categories': categories,
    }
    return render(request, 'home.html', context)


def about(request):
    skills_data = {
        'Python & Django': 90, 'Data Science & Analytics': 90,
        'HTML, CSS & JavaScript': 90, 'React JS': 80,
        'Java Programming': 80, 'Cloud Computing (AWS)': 80,
        'AI/ML & Generative AI': 80, 'Prompt Engineering': 80,
        'SQL & Database': 75, 'Git & GitHub': 75,
    }
    return render(request, 'about.html', {'skills_data': skills_data})


def course_list(request):
    courses = Course.objects.filter(is_active=True)
    categories = Category.objects.all()

    # Filters
    category_id = request.GET.get('category')
    course_type = request.GET.get('type')
    level = request.GET.get('level')
    search = request.GET.get('q')

    if category_id:
        courses = courses.filter(category_id=category_id)
    if course_type:
        courses = courses.filter(course_type=course_type)
    if level:
        courses = courses.filter(level=level)
    if search:
        courses = courses.filter(Q(title__icontains=search) | Q(description__icontains=search))

    context = {
        'courses': courses,
        'categories': categories,
        'selected_category': category_id,
        'selected_type': course_type,
        'selected_level': level,
        'search_query': search,
    }
    return render(request, 'courses/course_list.html', context)


def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug, is_active=True)
    modules = course.get_modules()
    reviews = course.reviews.filter(is_approved=True)
    is_enrolled = False
    user_progress = {}

    if request.user.is_authenticated:
        is_enrolled = Enrollment.objects.filter(user=request.user, course=course, status='active').exists()
        if is_enrolled:
            for module in modules:
                prog = ModuleProgress.objects.filter(user=request.user, module=module).first()
                user_progress[module.id] = prog.completed if prog else False

    # Show modules based on enrollment
    visible_modules = []
    for module in modules:
        if course.course_type == 'free' or is_enrolled or module.is_preview:
            visible_modules.append(module)

    context = {
        'course': course,
        'modules': visible_modules,
        'all_modules': modules,
        'reviews': reviews,
        'is_enrolled': is_enrolled,
        'user_progress': user_progress,
        'what_you_learn': course.what_you_learn.split('\n') if course.what_you_learn else [],
        'requirements': course.requirements.split('\n') if course.requirements else [],
    }
    return render(request, 'courses/course_detail.html', context)


@login_required
def enroll_course(request, slug):
    course = get_object_or_404(Course, slug=slug, is_active=True)

    if course.course_type == 'paid':
        return redirect('payment', slug=slug)

    enrollment, created = Enrollment.objects.get_or_create(
        user=request.user,
        course=course,
        defaults={'is_paid': False, 'status': 'active'}
    )

    if created:
        course.students_count += 1
        course.save()
        messages.success(request, f'✅ Successfully enrolled in {course.title}!')
    else:
        messages.info(request, f'You are already enrolled in {course.title}.')

    return redirect('course_detail', slug=slug)


@login_required
def module_detail(request, course_slug, module_id):
    course = get_object_or_404(Course, slug=course_slug, is_active=True)
    module = get_object_or_404(Module, id=module_id, course=course, is_active=True)

    # Check access
    is_enrolled = Enrollment.objects.filter(user=request.user, course=course, status='active').exists()
    if course.course_type == 'paid' and not is_enrolled and not module.is_preview:
        messages.error(request, '🔒 Please enroll in this course to access this module.')
        return redirect('course_detail', slug=course_slug)

    # Track access
    if is_enrolled:
        ModuleProgress.objects.get_or_create(user=request.user, module=module)

    modules = course.get_modules()
    progress_data = {}
    for m in modules:
        prog = ModuleProgress.objects.filter(user=request.user, module=m).first()
        progress_data[m.id] = prog.completed if prog else False

    # Get current module index for prev/next
    module_list = list(modules)
    current_idx = next((i for i, m in enumerate(module_list) if m.id == module.id), 0)
    prev_module = module_list[current_idx - 1] if current_idx > 0 else None
    next_module = module_list[current_idx + 1] if current_idx < len(module_list) - 1 else None

    # Progress for this course
    enrollment = Enrollment.objects.filter(user=request.user, course=course).first()

    context = {
        'course': course,
        'module': module,
        'modules': modules,
        'progress_data': progress_data,
        'prev_module': prev_module,
        'next_module': next_module,
        'enrollment': enrollment,
        'is_enrolled': is_enrolled,
    }
    return render(request, 'courses/module_detail.html', context)


@login_required
def mark_complete(request, course_slug, module_id):
    if request.method == 'POST':
        module = get_object_or_404(Module, id=module_id)
        progress, created = ModuleProgress.objects.get_or_create(
            user=request.user, module=module
        )
        progress.completed = True
        progress.completed_at = timezone.now()
        progress.save()

        # Check if course completed
        course = module.course
        total = course.total_modules()
        completed = ModuleProgress.objects.filter(
            user=request.user, module__course=course, completed=True
        ).count()

        if total > 0 and completed >= total:
            enrollment = Enrollment.objects.filter(user=request.user, course=course).first()
            if enrollment:
                enrollment.status = 'completed'
                enrollment.save()

        return JsonResponse({'success': True, 'progress': int((completed/total)*100) if total else 0})
    return JsonResponse({'success': False})


def events(request):
    upcoming_events = Event.objects.filter(is_active=True, event_date__gte=timezone.now())
    past_events = Event.objects.filter(is_active=True, event_date__lt=timezone.now())
    context = {
        'upcoming_events': upcoming_events,
        'past_events': past_events,
    }
    return render(request, 'events/events.html', context)


def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'🎉 Welcome to Ram Sir Platform, {user.first_name}!')
            return redirect('dashboard')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


@login_required
def dashboard(request):
    user = request.user
    enrollments = Enrollment.objects.filter(user=user, status__in=['active', 'completed']).select_related('course')
    recent_progress = ModuleProgress.objects.filter(user=user).order_by('-last_accessed')[:5]
    payments = Payment.objects.filter(user=user).order_by('-created_at')[:5]
    upcoming_events = Event.objects.filter(is_active=True, event_date__gte=timezone.now())[:3]

    # Stats
    total_enrolled = enrollments.count()
    completed_courses = enrollments.filter(status='completed').count()
    total_modules_done = ModuleProgress.objects.filter(user=user, completed=True).count()

    context = {
        'enrollments': enrollments,
        'recent_progress': recent_progress,
        'payments': payments,
        'upcoming_events': upcoming_events,
        'total_enrolled': total_enrolled,
        'completed_courses': completed_courses,
        'total_modules_done': total_modules_done,
    }
    return render(request, 'dashboard/dashboard.html', context)


@login_required
def profile(request):
    profile_obj, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile_obj, user=request.user)
        if form.is_valid():
            form.save()
            request.user.first_name = form.cleaned_data['first_name']
            request.user.last_name = form.cleaned_data['last_name']
            request.user.email = form.cleaned_data['email']
            request.user.save()
            messages.success(request, '✅ Profile updated successfully!')
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=profile_obj, user=request.user)

    return render(request, 'dashboard/profile.html', {'form': form, 'profile': profile_obj})


@login_required
def my_courses(request):
    enrollments = Enrollment.objects.filter(user=request.user).select_related('course')
    return render(request, 'dashboard/my_courses.html', {'enrollments': enrollments})


@login_required
def my_progress(request):
    enrollments = Enrollment.objects.filter(user=request.user, status__in=['active', 'completed'])
    progress_data = []
    for enrollment in enrollments:
        total = enrollment.course.total_modules()
        completed = enrollment.completed_modules_count()
        progress_data.append({
            'enrollment': enrollment,
            'total': total,
            'completed': completed,
            'percentage': enrollment.progress_percentage(),
        })
    return render(request, 'dashboard/progress.html', {'progress_data': progress_data})


@login_required
def my_history(request):
    payments = Payment.objects.filter(user=request.user).order_by('-created_at')
    enrollments = Enrollment.objects.filter(user=request.user).order_by('-enrolled_at')
    progress_history = ModuleProgress.objects.filter(user=request.user, completed=True).order_by('-completed_at')[:20]
    context = {
        'payments': payments,
        'enrollments': enrollments,
        'progress_history': progress_history,
    }
    return render(request, 'dashboard/history.html', context)


@login_required
def payment_page(request, slug):
    course = get_object_or_404(Course, slug=slug, course_type='paid', is_active=True)

    # Check if already enrolled
    if Enrollment.objects.filter(user=request.user, course=course, status='active').exists():
        messages.info(request, 'You are already enrolled in this course!')
        return redirect('course_detail', slug=slug)

    form = PaymentForm()
    context = {
        'course': course,
        'form': form,
        # Admin UPI details - update these
        'upi_id': 'ramsirdevix@upi',
        'phone': '9753528324',
    }
    return render(request, 'courses/payment.html', context)


@login_required
def payment_confirm(request, slug):
    course = get_object_or_404(Course, slug=slug, course_type='paid', is_active=True)
    if request.method == 'POST':
        form = PaymentForm(request.POST, request.FILES)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.user = request.user
            payment.course = course
            payment.amount = course.price
            payment.status = 'pending'
            payment.save()
            messages.success(request, '✅ Payment submitted! Admin will verify and activate your course within 24 hours.')
            return redirect('dashboard')
        else:
            messages.error(request, '❌ Please fill all required fields.')
    return redirect('payment', slug=slug)


def generate_ai_content(request):
    """Generate course content using Claude AI API"""
    if not request.user.is_staff:
        return JsonResponse({'error': 'Unauthorized'}, status=403)

    if request.method == 'POST':
        data = json.loads(request.body)
        topic = data.get('topic', '')
        content_type = data.get('content_type', 'explanation')

        try:
            from django.conf import settings
            api_key = settings.CLAUDE_API_KEY

            prompt = f"""You are Ram Sir, a technical trainer from Indore, India teaching {topic}.
Create a {content_type} for students. Make it:
- Clear and easy to understand with examples
- Include code examples if relevant
- Use simple Indian English
- Format with HTML tags for better display
- Be comprehensive but concise

Generate the content now:"""

            request_data = json.dumps({
                "model": "claude-sonnet-4-20250514",
                "max_tokens": 2000,
                "messages": [{"role": "user", "content": prompt}]
            }).encode('utf-8')

            req = urllib.request.Request(
                'https://api.anthropic.com/v1/messages',
                data=request_data,
                headers={
                    'Content-Type': 'application/json',
                    'x-api-key': api_key,
                    'anthropic-version': '2023-06-01'
                }
            )

            with urllib.request.urlopen(req) as response:
                result = json.loads(response.read())
                content = result['content'][0]['text']
                return JsonResponse({'content': content, 'success': True})

        except Exception as e:
            return JsonResponse({'error': str(e), 'success': False})

    return JsonResponse({'error': 'POST required'}, status=400)
