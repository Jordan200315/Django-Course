from django.shortcuts import render
# Create your views here.

def resume(request):
    context={}
    return render(request, "tem3/resume.html", context )