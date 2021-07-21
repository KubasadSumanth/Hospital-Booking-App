from django.contrib import admin
from .models import ToDoList,Item,Hospitals,Patients,Book
# Register your models here.
admin.site.register(ToDoList)
admin.site.register(Item)
admin.site.register(Hospitals)
admin.site.register(Patients)
admin.site.register(Book)