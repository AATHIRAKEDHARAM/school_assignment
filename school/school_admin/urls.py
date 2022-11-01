from django.urls import path

from . import views

app_name= "school_admin"
urlpatterns = [
    path("dashboard", views.dashboard,name="dashboard"),   
    path("add_mark", views.add_mark,name="add_mark"),   
    path("edit_mark", views.edit_mark,name="edit_mark"),   
]