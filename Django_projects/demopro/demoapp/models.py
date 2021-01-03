from django.db import models
import os


class User(models.Model):
    fname=models.CharField(max_length=50,default="")
    lname=models.CharField(max_length=50,default="")
    email=models.EmailField(default="")
    mobile=models.IntegerField(default="")

    def __str__(self):
        return self.fname



class myprofile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default="")
    address=models.CharField(max_length=50,blank=True)
    city=models.CharField(max_length=50,blank=True)

    def __str__(self):
        return self.address
    

def image_path(instance, filename):
    instance_id = str(instance.my_profile.id)
    return os.path.join('images', instance_id, filename)



class profilephoto(models.Model):
    my_profile = models.ForeignKey(myprofile, on_delete=models.CASCADE, related_name='profilephoto')
    photo = models.ImageField(upload_to=image_path, max_length=255)