from django.db import models


class student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    number = models.IntegerField()

    def __str__(self):
        return self.name
    