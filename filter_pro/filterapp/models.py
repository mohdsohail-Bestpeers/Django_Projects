from django.db import models
from django.contrib.auth.models import User


class event_user(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.IntegerField()

class event(models.Model):
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)
    e_user = models.ForeignKey(event_user, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)