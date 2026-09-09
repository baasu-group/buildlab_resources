from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def profile(request):
    data = {
    "name": "madhu",
    "age": "21",
    "course": "IT",
    "is_student":False,
    }
    return render(request, "core/profile.html",data)

def subject(request):
    data = {
        "subject": ["DJango","Networking","Database"]
    }
    return render(request, "core/subject.html",data)

def home(request):
    return render(request, "core/home.html")

def about(request):
    return HttpResponse("Hello this is about page.")

def contact(request):
    return HttpResponse("Contact Me <br> email:123@gmail.com")

def student(request):
    data = {
        "students": ["ram","sita","hari","sunny"]
    }
    return render(request, "core/student.html", data)
