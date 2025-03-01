from django.shortcuts import render
from django.views.generic import DeleteView, ListView
from .models import Course
from django.urls import reverse_lazy
# Create your views here.

class CourseListView(ListView):
    model = Course
    context_object_name = 'course'
    template_name = 'course_list.html'

class Course_delete(DeleteView):
    model = Course
    template_name = "delete_course.html"
    context_object_name = 'delete_course'
    success_url = reverse_lazy("course_list")
