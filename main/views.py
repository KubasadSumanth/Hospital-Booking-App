from django.shortcuts import render
#from django.http import httpResponse
from django.shortcuts import HttpResponse,HttpResponseRedirect
from .models import ToDoList,Item
from .models import Hospitals,Book,Patients

from .forms import CreateNewList
from .forms import HispitalForm

# Create your views here.
from django.shortcuts import redirect

import pyrebase


aboutdata = {"name":"tea"}
def profile(response):
    return render(response,"main/profile.html",{"name":"ls.name"})

def dashboard(response):
    user=response.user
    #report={}
    report=Patients.objects.filter(name=user.username)
    #try:
    #except Exception as e:
    #    print(e)
    if(user.is_authenticated):
        allhospitals=Hospitals.objects.all()
        bookings=Book.objects.all()


        config = {
            "apiKey": "AIzaSyB2AfIXtvkzRWk7kdcR4dM0Kn6EA6p6Nn8",
            "authDomain": "health-monitoring-426c4.firebaseapp.com",
            "databaseURL": "https://health-monitoring-426c4-default-rtdb.firebaseio.com",
            "projectId": "health-monitoring-426c4",
            "storageBucket": "health-monitoring-426c4.appspot.com",
            "messagingSenderId": "166620034684",
            "appId": "1:166620034684:web:da7dfb4534b821ecd93bf9",
        }

        firebase=pyrebase.initialize_app(config)
        #authe=firebase.auth()
        database=firebase.database()
        bpm=database.child('BPM').get().val()
        spo=database.child('SPO2').get().val()
        temp=database.child('TEMP').get().val()




        #print(allhospitals)
        if response.method == "POST":
            form = HispitalForm(response.POST)
            if form.is_valid():
                #print(form)
                hospital_name = form.cleaned_data["hospital_name"]
                tags = form.cleaned_data["tags"]
                numSeats = form.cleaned_data["numSeats"]
                doctorName = form.cleaned_data["doctorName"]
                target = Hospitals(hospitalName=hospital_name,specialities=tags,noOfSeats=numSeats,doctorName=doctorName)
                #t = ToDoList(name=n)
                print(target)
                target.save()
                #response.user.todolist_set.create(name=n)
                #print(response.user.hospitals.add(target))
                #.user.todolist.add(t)
                #HttpResponseRedirect("/%i" %t.id)
                return HttpResponseRedirect('#')
        form = HispitalForm()
        return render(response,"main/dashboard.html",{"report":report,"user":user,'form': form,'hs':allhospitals,"bookings":bookings,"bpm":bpm,"spo":spo,"temp":temp})
    else:
        return redirect('/login')

def home(response):
    user=response.user
    if(user.is_authenticated):
        return render(response,"main/dashboard.html",{"user":user})
    else:
        return redirect('/login')

def hospitalopened(response,hname):
    allhospitals=Hospitals.objects.all()

    ls=Hospitals.objects.get(hospitalName=hname)
    return render(response,"main/hospitalopened.html",{"name":ls})
    
def book(request):
    name=request.POST.get("hname","NotValue")
    h=Hospitals.objects.get(hospitalName=name)
    h.noOfSeats-=1
    h.save()
    print(h)
    username=request.POST.get("username","NotValue")
    email=request.POST.get("email","NotValue")
    consulttext=request.POST.get("consulttext","NotValue")
    doctorName=request.POST.get("doctorName","NotValue")
    #print(username)
    b=Book(hospitalName=name,username=username,email=email,consulttext=consulttext,doctorName=doctorName)
    b.save()
    return redirect("dashboard")
def casestudy(request):
    name=request.POST.get("hospitalName","NotValue")
    h=Hospitals.objects.get(hospitalName=name)
    h.noOfSeats+=1
    h.save()
    username=request.POST.get("username","NotValue")
    consulttext=request.POST.get("casedata","NotValue")
    c=Patients(name=username,casestudydata=consulttext)
    print(c.casestudydata)
    c.save()
    Book.objects.filter(username=username).delete()
    return redirect("dashboard")



#Below Used methods are used for understanding purpose only



def index(response,id):
    ls=ToDoList.objects.get(id=id)
    return render(response,"main/base.html",{"name":ls.name})

    #return HttpResponse("<h1>tech with Sumanth??? %s</h1>"%ls.name)
def start(response):
    return HttpResponse("<h1>Welcome to start page</h1>")


def view(response):
    return render(response,"main/view.html",{"name":"ls.name"})

def v1(response):
    return render(response,"main/base.html",{"name":"ls.name"})


def homes(response,id):
    ls=ToDoList.objects.get(id=id)
    print(ls)
    lists = (Item.objects.filter(todolist=ls))
    print(lists)
    if response.method == "POST":
        print(response.POST)
        if response.POST.get("save"):
            for item in ls.item_set.all():
                if response.POST.get("c"+str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False
                item.save()
        elif response.POST.get("newItem"):
            txt = response.POST.get("new")
            if(len(txt)>2):
                ls.item_set.create(text=txt,complete=False)
            else:
                print("invalid input")

    return render(response,"main/list.html",{"ls":ls})
    
def create(response):
    usrdata = response.user

    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
            #response.user.todolist_set.create(name=n)
            response.user.todolist.add(t)
        return HttpResponseRedirect("/%i" %t.id)
    formas = CreateNewList()
    return render(response,"main/create.html",{"form":formas})