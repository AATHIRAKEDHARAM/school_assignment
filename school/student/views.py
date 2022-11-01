from django.shortcuts import render

# Create your views here.
from .import views


def dashboard(request):
    return render(request, "student/dashboard.html")


def profile_info(request):
    return render(request, "student/profile_info.html")


def edit_details(request):
    return render(request, "student/edit_details.html")
