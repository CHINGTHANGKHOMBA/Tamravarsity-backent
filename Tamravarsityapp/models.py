from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField  # For rich text support

# Create your models here.

    
class UserCustomer(models.Model):
    user_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, null=True, blank=True)  # Allow nulls initially
    address = models.TextField(blank=True, null=True)
    is_activate = models.BooleanField(default=False)

    def __str__(self):
        return self.user_name


class Courses(models.Model):
    COURSE_TYPES = [
        ('online', 'Online'),
        ('offline', 'Offline'),
        ('hybrid', 'Hybrid'),
    ]

    course_name = models.CharField(max_length=400)
    course_type = models.CharField(max_length=10, choices=COURSE_TYPES, default='online')
    course_img = models.FileField(upload_to="courseImg/", blank=True, null=True, default="no_image/noimage.png")
    course_details = RichTextField()  # ✅ Rich text field

    def __str__(self):
        return self.course_name

