from django.contrib import admin
from .models import student, teacher
# Register your models here.

class studentAdmin(admin.ModelAdmin):
    list_display=['name','rollno','marks']

class teacherAdmin(admin.ModelAdmin):
    list_display=['name','description']

admin.site.register(student,studentAdmin)
admin.site.register(teacher,teacherAdmin)