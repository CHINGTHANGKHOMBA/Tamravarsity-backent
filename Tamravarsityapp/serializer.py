from rest_framework import serializers
from .models import UserCustomer, Courses

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCustomer
        fields = "__all__"

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'