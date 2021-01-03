from django.shortcuts import render
from .models import abc
# Create your views here.

def index(request):
    if request.method=='POST':
        s=abc()
        s.fname=request.POST.get('fname')
        s.lname=request.POST.get('lname')
        s.image=request.POST.get('image')
        s.save()
        return render(request,'showdeta.html')
    else:
        return render(request,'index.html')



def result(request):
    d=abc.objects.all()
    return render(request,'result.html',{'data':d})