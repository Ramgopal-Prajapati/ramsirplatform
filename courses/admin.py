from django.contrib import admin
from django.utils.html import format_html
from django.utils import timezone
from .models import (
    UserProfile, Category, Course, Module,
    Enrollment, ModuleProgress, Payment, Event, Review
)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'city', 'college', 'created_at']
    search_fields = ['user__username', 'user__email', 'phone']


class ModuleInline(admin.StackedInline):
    model = Module
    extra = 1
    fields = ['title', 'order', 'content_type', 'youtube_url', 'text_content', 'image', 'image_url', 'image_caption', 'duration_minutes', 'is_preview', 'is_active']
    show_change_link = True


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon', 'color']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'course_type', 'price', 'level', 'students_count', 'is_featured', 'is_active', 'created_at']
    list_filter = ['course_type', 'level', 'is_featured', 'is_active', 'category']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ModuleInline]
    list_editable = ['is_featured', 'is_active', 'course_type']
    fieldsets = (
        ('Basic Info', {
            'fields': ('title', 'slug', 'category', 'short_description', 'description')
        }),
        ('Media', {
            'fields': ('thumbnail', 'thumbnail_url')
        }),
        ('Pricing & Type', {
            'fields': ('course_type', 'price', 'level', 'duration')
        }),
        ('Instructor', {
            'fields': ('instructor_name', 'instructor_bio')
        }),
        ('Details', {
            'fields': ('what_you_learn', 'requirements', 'rating', 'students_count')
        }),
        ('Status', {
            'fields': ('is_featured', 'is_active')
        }),
    )


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'order', 'content_type', 'duration_minutes', 'is_active', 'is_preview']
    list_filter = ['course', 'content_type', 'is_active']
    search_fields = ['title', 'course__title']
    list_editable = ['order', 'is_active']
    fieldsets = (
        ('Basic Info', {
            'fields': ('course', 'title', 'description', 'order', 'content_type', 'is_preview', 'is_active', 'duration_minutes')
        }),
        ('Video Content', {
            'fields': ('youtube_url',),
            'description': 'Paste YouTube URL or Video ID here. It will be embedded automatically.'
        }),
        ('Text Content', {
            'fields': ('text_content',),
            'description': 'Supports HTML formatting for rich content.'
        }),
        ('Image Content', {
            'fields': ('image', 'image_url', 'image_caption'),
        }),
    )


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['user', 'course', 'status', 'is_paid', 'amount_paid', 'enrolled_at']
    list_filter = ['status', 'is_paid', 'course']
    search_fields = ['user__username', 'course__title']
    list_editable = ['status', 'is_paid']


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['user', 'course', 'amount', 'status', 'payment_method', 'created_at', 'verify_button']
    list_filter = ['status', 'payment_method']
    search_fields = ['user__username', 'transaction_id']
    list_editable = ['status']
    readonly_fields = ['created_at', 'verified_at']
    fieldsets = (
        ('Payment Info', {
            'fields': ('user', 'course', 'amount', 'status', 'payment_method', 'transaction_id', 'upi_id')
        }),
        ('Evidence', {
            'fields': ('screenshot', 'notes')
        }),
        ('Verification', {
            'fields': ('verified_by', 'verified_at', 'created_at')
        }),
    )

    def verify_button(self, obj):
        if obj.status == 'pending':
            return format_html(
                '<a class="button" href="/admin/courses/payment/{}/change/" style="background:#28a745;color:white;padding:3px 8px;border-radius:3px;">Verify</a>',
                obj.pk
            )
        elif obj.status == 'completed':
            return format_html('<span style="color:green;">✓ Verified</span>')
        return obj.status
    verify_button.short_description = 'Action'

    def save_model(self, request, obj, form, change):
        if obj.status == 'completed' and not obj.verified_at:
            obj.verified_at = timezone.now()
            obj.verified_by = request.user
            # Auto-enroll student
            enrollment, created = Enrollment.objects.get_or_create(
                user=obj.user,
                course=obj.course,
                defaults={'is_paid': True, 'amount_paid': obj.amount, 'status': 'active'}
            )
            if not created:
                enrollment.is_paid = True
                enrollment.amount_paid = obj.amount
                enrollment.status = 'active'
                enrollment.save()
        super().save_model(request, obj, form, change)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'event_type', 'event_date', 'location', 'is_free', 'seats_available', 'is_active']
    list_filter = ['is_free', 'is_active', 'event_type']
    list_editable = ['is_active']
    fieldsets = (
        ('Event Info', {
            'fields': ('title', 'description', 'event_type', 'event_date', 'location')
        }),
        ('Media', {
            'fields': ('image', 'image_url')
        }),
        ('Registration', {
            'fields': ('registration_link', 'is_free', 'seats_available', 'is_active')
        }),
    )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'course', 'rating', 'created_at', 'is_approved']
    list_editable = ['is_approved']
    list_filter = ['rating', 'is_approved']
