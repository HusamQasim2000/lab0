from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    name={"fname":"Husam"}
    return render(request,'index.html',name)

def home(request):
    return render(request,'home.html')

def list_students(request):
    students={
        "name":"Husam",
        "marks":[92,88,87,80],
        "eachsub":{"software engineering":93,"Image processing":98, "Client and Server Programming":97
        }
    }
    return render(request,'showstudents.html',students)

def edit_students(request):
    students={
        "total":287,
        "marks":{
                 "software engineering":93,
                 "Image processing":98,
                 "Client and Server Programming":97
        }
    }
    return render(request,'editstudents.html',students)

def delete_students(request):
    return render(request,'deletestudents.html')
