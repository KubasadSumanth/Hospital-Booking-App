from django.urls import path
from . import views

urlpatterns = [
    #path("",views.home,name="home"),
    #path("home/",views.home,name="home"),
    #path("<str:name>",views.index,name="index"),
    #path("create/",views.create,name="create"),
    #path("<int:id>",views.homes,name="homes"),
    path("",views.dashboard,name="dashboard"),
    path("dashboard/",views.dashboard,name="dashboard"),
    path("dashboard/book/appt",views.book,name="book"),
    path("dashboard/patient/casestudy",views.casestudy,name="casestudy"),
    path("dashboard/<str:hname>",views.hospitalopened,name="hospitalopened"),
    path("profile/",views.profile,name="profile"),

    #path("start/",views.start,name="start"),
    #path("home/",views.v1,name="view 1"),
    #path("view/",views.view,name="view"),
]