from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from courses import views as course_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', course_views.home, name='home'),
    path('courses/', course_views.course_list, name='course_list'),
    path('courses/<slug:slug>/', course_views.course_detail, name='course_detail'),
    path('courses/<slug:slug>/enroll/', course_views.enroll_course, name='enroll_course'),
    path('courses/<slug:course_slug>/module/<int:module_id>/', course_views.module_detail, name='module_detail'),
    path('courses/<slug:course_slug>/module/<int:module_id>/complete/', course_views.mark_complete, name='mark_complete'),
    path('events/', course_views.events, name='events'),
    path('about/', course_views.about, name='about'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', course_views.register, name='register'),
    path('dashboard/', course_views.dashboard, name='dashboard'),
    path('dashboard/profile/', course_views.profile, name='profile'),
    path('dashboard/my-courses/', course_views.my_courses, name='my_courses'),
    path('dashboard/progress/', course_views.my_progress, name='my_progress'),
    path('dashboard/history/', course_views.my_history, name='my_history'),
    path('payment/<slug:slug>/', course_views.payment_page, name='payment'),
    path('payment/<slug:slug>/confirm/', course_views.payment_confirm, name='payment_confirm'),
    path('api/ai-content/', course_views.generate_ai_content, name='ai_content'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Customize admin
admin.site.site_header = "Ram Sir Platform Admin"
admin.site.site_title = "Ram Sir Admin"
admin.site.index_title = "Welcome to Ram Sir Course Management"
