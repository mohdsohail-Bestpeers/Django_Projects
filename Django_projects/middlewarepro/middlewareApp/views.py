from django.shortcuts import render,HttpResponse
from django.template.response import TemplateResponse

# Create your views here.

def home(request):
    print("i am view")
    return HttpResponse("this is home page")

#this function is for exception middleware
def excp(request):
    print("i am Exception view ")
    a = 10/0
    return HttpResponse("this is exception page")


#this function is for template middleware 
def user_info(request):
    print("i am user info")
    context={'name':'rahul'}
    return TemplateResponse(request,'user.html',context)