from traceback import format_tb
from django.contrib import admin

# Register your models here.
from .models import User, Courses


from django.contrib import admin
from .models import UserCustomer, Courses  # Import models

# @admin.register(UserCustomer)
# class UserCustomer(admin.ModelAdmin):
#     list_display = ('user_name', 'phone_number', 'is_active')  # Columns in admin panel
#     search_fields = ('user_name', 'phone_number')  # Searchable fields
#     list_filter = ('is_active',)  # Filter by active status

@admin.register(UserCustomer)
class UserCustomerAdmin(admin.ModelAdmin):
    list_display = ("user_name", "email", "is_activate")  # Display these fields in the admin panel
    search_fields = ("user_name", "email")  # Enable search

@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'course_type')  # Columns in admin panel
    search_fields = ('course_name',)  # Searchable fields
    list_filter = ('course_type',)  # Filter by course type

    # def image_preview(self, obj):
    #     if obj.course_img:  # Check if image exists
    #         return format_tb(f'<img src="{obj.course_img.url}" />')
    #     return "No Image"

    # image_preview.short_description = "Course Image"