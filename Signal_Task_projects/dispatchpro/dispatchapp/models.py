from django.db import models


class post(models.Model):

    Tittle=models.CharField(max_length=50)

    def __str__(self):
        return self.Tittle

