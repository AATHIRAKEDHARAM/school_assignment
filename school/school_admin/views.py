from django.shortcuts import render

# Create your views here.



def dashboard(request):
    return render(request, "school_admin/dashboard.html")

def add_mark(request):
    return render(request, "school_admin/add_mark.html")

def edit_mark(request):
    return render(request, "school_admin/edit_mark.html")