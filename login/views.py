import json
from django.shortcuts import render,redirect

from login.models import Userdata
from .forms import FileForm, RegisterForm
from django.core.files.uploadedfile import UploadedFile
# Create your views here.

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    else:
        form = RegisterForm()
    return render(response, 'register/register.html', {"form": form} )

def home(request):
    if request.method == 'POST':
        form = FileForm(request.POST)  
        data = request.POST['content-target']
        data_dict =  json.loads(data)
        for item in data_dict:
            c, new = Userdata.objects.get_or_create(**item)
            # optional:
            if not new:
                print("Entry already in the DB:")
                print(c)
        if form.is_valid():  
            return redirect("/")
    else:  
        student = FileForm() 
    return render(request, 'base/home.html',{"form":student})

def data(request):
    if request.user.is_authenticated:
        user = request.user
        queryset = Userdata.objects.all()

        context = {
            "object_list": queryset,
            "user": user
        }
    return render(request, 'base/data.html',context)
    
