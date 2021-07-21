from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm

from .forms import RegisterForm

# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            print(form)
            form.save()
            return redirect("dashboard")
    else:        
        form = RegisterForm()

    return render(response,"register/register.html",{"form":form})