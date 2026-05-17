from django.contrib import admin
from .models import Student
# Register your models here.
class Studentadmin(admin.ModelAdmin):
    list_display=['name','age','course','email']
    search_fields=['name','course']
    list_filter=['age']
admin.site.register(Student,Studentadmin)
