from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import get_users, create_user, get_courses, get_course_by_id, google_auth


urlpatterns = static(settings.STATIC_ROOT, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + [
    path('users/', get_users, name='get_users'),
    path('users/create/', create_user, name='create_user'),
    path('courses/', get_courses, name='get_courses'),
    path('courses/<int:id>/', get_course_by_id, name='get_course_by_id'),
    path("auth/google/", google_auth, name="google_auth"),
]