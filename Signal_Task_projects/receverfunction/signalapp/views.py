from django.shortcuts import render, HttpResponse
from django.core.signals import request_finished
from django.dispatch import receiver



def home(request):
    return HttpResponse("This is Recever Fuction")


@receiver(request_finished)
def post_request_reciver(sender, **kwargs):
    print("Request finished!")

