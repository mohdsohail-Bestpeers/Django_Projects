from django.contrib import admin
from .models import User,myprofile, profilephoto


admin.site.register(User)
admin.site.register(myprofile)
admin.site.register(profilephoto)