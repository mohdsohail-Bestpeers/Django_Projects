from django.db import models



class abc(models.Model):
    fname=models.CharField(max_length=50,blank=True)
    lname=models.CharField(max_length=50,blank=True)
    image=models.ImageField(upload_to = 'images', max_length=255)




    