from django.shortcuts import render, HttpResponse
from .forms import SignupForm


# Create your views here.

def signup(request):
    if request.method == "POST" and request.is_ajax():
        form = SignupForm(request.POST)
        data = {}
        if form.is_valid():
            data['success'] = True
            return HttpResponse(json.dumb(data),context_type='application/json')
        else:
            data['success'] = False
            return HttpResponse(json.dumb(data),context_type='application/json')
       
    else:
        form = SignupForm()
        return render(request,'signup_form.html',{'form':form})