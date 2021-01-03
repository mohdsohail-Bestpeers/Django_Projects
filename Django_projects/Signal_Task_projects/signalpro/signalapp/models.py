from django.db import models
from django.db.models.signals import post_save, pre_save, post_delete 

# Create your models here.

class post(models.Model):

    Tittle=models.CharField(max_length=50)

    def __str__(self):
        return self.Tittle

def save_post(sender, instance, **kwargs):
    print("post save is call")

def save_pre(sender, instance, **kwargs):
    print("pre save is call")


#create delete function
def after_delete_post(sender, instance, **kwargs):
    print("you delete somthing")

post_save.connect(save_post, sender=post)

#this is a pre_save 
pre_save.connect(save_pre, sender=post) 

#the first 'somthing' is being called at the begning of the save method 
#the secound 'somthing' is being called at the end of the save method 

post_delete.connect(after_delete_post, sender=post)