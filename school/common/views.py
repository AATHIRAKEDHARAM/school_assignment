
from django.shortcuts import render,redirect
from .models import *


# Create your views here.


def home(request):
    return render(request, "common/home.html")


def admin_reg(request):
    msg=''
    if request.method=="POST":
        name = request.POST["name"]
        dob = request.POST["dob"]
        phone = request.POST["phone"]
        username = request.POST["username"]
        password = request.POST["password"]
        image = request.FILES["image"]

        user_exists=AdminReg.objects.filter(username=username).exists()
        if user_exists:
            msg="username already exists"
        else:
            admin=AdminReg(name=name,dob=dob,phone=phone,username=username,password=password,image=image)  
            admin.save()  
            return redirect("common:admin_login")
        

    return render(request, "common/admin_reg.html",{'msg':msg})

def admin_login(request):
    msg=''
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]

        admin_exist=AdminReg.objects.filter(username=username,password=password)
        if admin_exist:
            admin_details = AdminReg.objects.get(username=username,password=password)
            request.session['admin_id'] = admin_details.id
            return redirect("school_admin:dashboard")
        else:
            msg="invaild username or password"
    return render(request, "common/admin_login.html",{"msg":msg})


def student_reg(request):
    msg=''
    if request.method=="POST":
        name = request.POST["name"]
        dob = request.POST["dob"]
        phone = request.POST["phone"]
        username = request.POST["username"]
        password = request.POST["password"]
        image = request.FILES["image"]

        user_exists=StudentReg.objects.filter(username=username).exists()
        if user_exists:
            msg="username already exists"
        else:
            student=StudentReg(name=name,dob=dob,phone=phone,username=username,password=password,image=image)  
            student.save()  
            return redirect("common:student_login")
    return render(request, "common/student_reg.html" ,{'msg':msg} )


def student_login(request):
    msg=''
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]

        student_exists=StudentReg.objects.filter(username=username,password=password)
        if student_exists:
            student_details = StudentReg.objects.get(username=username,password=password)
            request.session['student_id'] = student_details.id
            return redirect("student:dashboard")
        else:
            msg="invaild username or password"
    return render(request, "common/student_login.html")
