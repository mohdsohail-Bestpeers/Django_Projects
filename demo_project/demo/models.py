from django.db import models


class student(models.Model):
    name = models.CharField(max_length=20, blank=True)
    rollno = models.IntegerField(null=True, blank=True)
    marks = models.IntegerField(null=True)
   
class teacher(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

