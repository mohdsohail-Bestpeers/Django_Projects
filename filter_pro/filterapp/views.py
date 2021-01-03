from django.shortcuts import render
from .models import event
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect


def detail(request, x):
    if request.user.is_authenticated:
        objs = event.objects.filter(publisher__first_name=x)
        return render(request, 'publisher1.html', {'objs':objs})
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