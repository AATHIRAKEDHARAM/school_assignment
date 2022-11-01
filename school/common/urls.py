from django.urls import path

from . import views

app_name= "common"
urlpatterns = [
    path("", views.home, name="home"),
    path("admin_reg", views.admin_reg ,name="admin_reg"),   
    path("student_reg", views.student_reg ,name="student_reg"),
    path("admin_login", views.admin_login ,name="admin_login"),
    path("student_login", views.student_login ,name="student_login"),
]