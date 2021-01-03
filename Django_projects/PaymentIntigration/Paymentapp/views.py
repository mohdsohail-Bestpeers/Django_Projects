from django.shortcuts import render
from .models import EventUser, Event, Address, event_photo
from .forms import event_user_form, event_form, address_form, event_photo_form
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def detail(request, x):
    if request.user.is_authenticated:
        objs = Event.objects.filter(publisher__first_name=x, payment_status='done')
        if request.method == 'POST':
            form1 = event_user_form(request.POST)
            form2 = event_form(request.POST)
            form3 = address_form(request.POST)
            form4 = event_photo_form(request.POST, request.FILES)
            obj = User.objects.get(first_name=x)
            if form1.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid():
                #form1
                event_user_obj = form1.save()
                #form2 
                form2.save(commit=False)
                form2.instance.event_user = event_user_obj
                form2.instance.publisher = obj
                event_obj = form2.save()
                #form3
                form3.save(commit=False)
                form3.instance.event = event_obj
                form3.save()
                #form4
                form4.save(commit=False)
                form4.instance.event = event_obj
                form4.save()
                return HttpResponseRedirect('/payment/')
        else:
            form1 = event_user_form()
            form2 = event_form()
            form3 = address_form()
            form4 = event_photo_form()
        return render(request, 'result.html', {'objs':objs, 'form1':form1, 'form2':form2, 'form3':form3, 'form4':form4})
    else:
        return HttpResponseRedirect('/login/')

def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user != None:
                    login(request, user)
                    return HttpResponseRedirect('/'+user.first_name+'/detail/')
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'form':form})
    else:
        return HttpResponseRedirect('/'+request.user.first_name+'/detail/')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def payment(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            obj = Event.objects.get(publisher__first_name=request.user.first_name, payment_status='pending')
            obj.payment_status = 'done'
            obj.save()
            return HttpResponseRedirect('/'+request.user.first_name+'/detail/')
        return render(request, 'payment.html')
    else:
        return HttpResponseRedirect('/login/')