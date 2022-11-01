from django.urls import path

from . import views

app_name= "student"
urlpatterns = [
    path("dashboard", views.dashboard, name="dashboard"),
    path("profile_info", views.profile_info ,name="profile_info"),   
    path("edit_details", views.edit_details ,name="edit_details"),
]