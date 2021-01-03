from django.db import models


# Create your models here.

class post(models.Model):

    Tittle=models.CharField(max_length=50)

    def __str__(self):
        return self.Tittle
