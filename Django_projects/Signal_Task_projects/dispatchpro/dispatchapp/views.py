from django.shortcuts import render, HttpResponse
from django.core.signals import request_finished
from django.dispatch import receiver, Signal
from .models import post #this module is for timstamp 

request_counter_signal=Signal(providing_args=['timestamp'])

def home(request):
    request_counter_signal.send(sender=post, timestamp='2019-10-10')
    return HttpResponse("Here's the Response")


@receiver(request_finished)
def post_request_reciver(sender, **kwargs):
    print("Request finished!")


@receiver(request_counter_signal)
def post_counter_signal_reciver(sender, **kwargs):
    print(kwargs)
