from django.contrib import admin
from django.urls import path, include
from .views import Course_delete, CourseListView

urlpatterns = [
    path("course/", CourseListView.as_view(), name="course_list"),
    path("course/delete/<str:pk>/", Course_delete.as_view(),name="delete_course")
]