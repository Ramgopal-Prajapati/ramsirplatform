from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=15, blank=True)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    city = models.CharField(max_length=100, blank=True)
    college = models.CharField(max_length=200, blank=True)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

    def get_avatar_url(self):
        if self.avatar:
            return self.avatar.url
        return '/static/images/default-avatar.png'


class Category(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, default='fas fa-code')
    color = models.CharField(max_length=20, default='#ff6b35')

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Course(models.Model):
    LEVEL_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('all', 'All Levels'),
    ]
    TYPE_CHOICES = [
        ('free', 'Free'),
        ('paid', 'Paid'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    short_description = models.CharField(max_length=300)
    thumbnail = models.ImageField(upload_to='course_thumbnails/', blank=True, null=True)
    thumbnail_url = models.URLField(blank=True, help_text="Or paste image URL here")
    course_type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='free')
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    level = models.CharField(max_length=15, choices=LEVEL_CHOICES, default='all')
    duration = models.CharField(max_length=50, blank=True, help_text="e.g. 20 hours")
    instructor_name = models.CharField(max_length=100, default='Ram Sir (Ramgopal Prajapati)')
    instructor_bio = models.TextField(blank=True)
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    students_count = models.IntegerField(default=0)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=4.9)
    what_you_learn = models.TextField(blank=True, help_text="One point per line")
    requirements = models.TextField(blank=True, help_text="One requirement per line")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-is_featured', '-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        if self.thumbnail_url:
            return self.thumbnail_url
        return '/static/images/default-course.png'

    def get_modules(self):
        return self.modules.filter(is_active=True).order_by('order')

    def total_modules(self):
        return self.modules.filter(is_active=True).count()


class Module(models.Model):
    CONTENT_TYPE_CHOICES = [
        ('video', 'YouTube Video'),
        ('text', 'Text Content'),
        ('image', 'Image'),
        ('mixed', 'Mixed Content'),
    ]

    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0)
    content_type = models.CharField(max_length=10, choices=CONTENT_TYPE_CHOICES, default='mixed')

    # Video content
    youtube_url = models.URLField(blank=True, help_text="YouTube video URL or ID")

    # Text content (supports HTML/Markdown)
    text_content = models.TextField(blank=True, help_text="Rich text content, supports HTML")

    # Image content
    image = models.ImageField(upload_to='module_images/', blank=True, null=True)
    image_url = models.URLField(blank=True, help_text="Or paste image URL")
    image_caption = models.CharField(max_length=300, blank=True)

    # Duration and metadata
    duration_minutes = models.IntegerField(default=0, help_text="Duration in minutes")
    is_active = models.BooleanField(default=True)
    is_preview = models.BooleanField(default=False, help_text="Free preview for paid courses?")

    # AI-generated content flag
    ai_generated = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.course.title} - {self.title}"

    def get_youtube_embed(self):
        """Convert YouTube URL to embed URL"""
        if not self.youtube_url:
            return ''
        url = self.youtube_url.strip()
        # Handle various YouTube URL formats
        if 'youtu.be/' in url:
            video_id = url.split('youtu.be/')[-1].split('?')[0]
        elif 'youtube.com/watch?v=' in url:
            video_id = url.split('v=')[-1].split('&')[0]
        elif 'youtube.com/embed/' in url:
            return url
        else:
            video_id = url  # Assume it's just the video ID
        return f"https://www.youtube.com/embed/{video_id}?rel=0&modestbranding=1"

    def get_image(self):
        if self.image:
            return self.image.url
        return self.image_url


class Enrollment(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    enrolled_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='active')
    is_paid = models.BooleanField(default=False)
    amount_paid = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)

    class Meta:
        unique_together = ['user', 'course']

    def __str__(self):
        return f"{self.user.username} → {self.course.title}"

    def progress_percentage(self):
        total = self.course.total_modules()
        if total == 0:
            return 0
        completed = ModuleProgress.objects.filter(
            user=self.user,
            module__course=self.course,
            completed=True
        ).count()
        return int((completed / total) * 100)

    def completed_modules_count(self):
        return ModuleProgress.objects.filter(
            user=self.user,
            module__course=self.course,
            completed=True
        ).count()


class ModuleProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)
    last_accessed = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['user', 'module']

    def __str__(self):
        return f"{self.user.username} - {self.module.title}"


class Payment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
        ('refunded', 'Refunded'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='pending')
    transaction_id = models.CharField(max_length=100, blank=True)
    payment_method = models.CharField(max_length=50, blank=True, help_text="UPI/Card/etc")
    upi_id = models.CharField(max_length=100, blank=True)
    screenshot = models.ImageField(upload_to='payment_screenshots/', blank=True, null=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    verified_at = models.DateTimeField(null=True, blank=True)
    verified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='verified_payments')

    def __str__(self):
        return f"{self.user.username} - {self.course.title} - ₹{self.amount}"


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    event_date = models.DateTimeField()
    event_type = models.CharField(max_length=50, default='Workshop')
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)
    image_url = models.URLField(blank=True, help_text="Or paste image URL")
    registration_link = models.URLField(help_text="Google Form link for registration")
    location = models.CharField(max_length=200, blank=True, default='Online (Live Session)')
    is_free = models.BooleanField(default=True)
    seats_available = models.IntegerField(default=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['event_date']

    def __str__(self):
        return self.title

    def is_upcoming(self):
        return self.event_date > timezone.now()

    def get_image(self):
        if self.image:
            return self.image.url
        if self.image_url:
            return self.image_url
        return '/static/images/default-event.png'


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=5)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=True)

    class Meta:
        unique_together = ['user', 'course']

    def __str__(self):
        return f"{self.user.username} - {self.course.title} ({self.rating}★)"
