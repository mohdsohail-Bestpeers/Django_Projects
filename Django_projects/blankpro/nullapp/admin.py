from django.contrib import admin
from .models import abc



class abcAdmin(admin.ModelAdmin):
    list_display=('fname','lname')


admin.site.register(abc,abcAdmin)