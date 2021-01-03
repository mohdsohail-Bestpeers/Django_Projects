from django.shortcuts import render
from .models import myprofile
from . forms import UserForm, myprofileForm
from django.http import HttpResponseRedirect
from django.urls import reverse




def result(request):
    d=myprofile.objects.all()
    #return render(request,'result.html',{'data':d})
    return render(request,'index.html',{'data':d})


def form1(request):
    form1=UserForm()
    if request.method == 'POST':
        form1 = UserForm(request.POST)
        if form1.is_valid():  
            form1.save()
            return HttpResponseRedirect(reverse('form2')) 
    return render(request, 'form1.html', {'form1':form1})


def form2(request):
    form = myprofileForm()
    if request.method == 'POST':
        form = myprofileForm(request.POST)
        if form.is_valid():
           form.save()
           form = myprofileForm()
    return render(request, 'form2.html', {'form':form})


