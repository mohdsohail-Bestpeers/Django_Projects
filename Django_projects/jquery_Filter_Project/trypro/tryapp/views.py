from django.shortcuts import render
from .models import student
from django.template.loader import render_to_string
from django.http import JsonResponse


def studentResult(request):
    form = student.objects.all()
    return render(request,'result.html',{'posts':form})


def find_data(request):
    if request.method == "POST":
        srch = request.POST.get("srch")
        srch2 = request.POST.get("srch2")
        obj = student.objects.filter(name__icontains=srch, email__icontains=srch2).values()
        html = render_to_string('post.html', context={'posts':obj}, request=request)
        return JsonResponse({'status':200, 'posts':html})
        
    else:
        return JsonResponse({'status':400})

      