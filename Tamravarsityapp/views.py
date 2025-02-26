from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import UserCustomer, Courses
from .serializer import UserSerializer, CourseSerializer

@api_view(['GET'])
def get_users(request):
    users = UserCustomer.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data, content_type="application/json")  # ✅ Ensures JSON response

@api_view(["POST"])
def google_auth(request):
    print("📩 Received Data:", request.data)  # Debugging log

    data = request.data
    email = data.get("email")  

    try:
        # Check if user exists
        user = UserCustomer.objects.get(email=email)
        message = "User logged in successfully"
        status_code = status.HTTP_200_OK
        created = False
    except UserCustomer.DoesNotExist:
        # Create user if not found
        user = UserCustomer.objects.create(
            user_name=data.get("user_name"),
            email=email,
            address=data.get("address", ""),
            is_activate=True,
        )
        message = "User created successfully"
        status_code = status.HTTP_201_CREATED
        created = True

    # Serialize user data
    serializer = UserSerializer(user)

    return Response(
        {"message": message, "user": serializer.data},
        status=status_code
    )

@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "User created successfully", "user": serializer.data}, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_courses(request):
    courses = Courses.objects.all()
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data, content_type="application/json")


@api_view(['GET'])
def get_course_by_id(request, id):
    try:
        course = Courses.objects.get(id=id)  # Fetch course by ID
        serializer = CourseSerializer(course)
        return Response(serializer.data)
    except Courses.DoesNotExist:
        return Response({"error": "Course not found"}, status=404)  # Return error if not found
    
