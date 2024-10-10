from django.shortcuts import render

# Create your views here.


# Create your views here.

def portfolio(request):
    context={}
    return render(request, "tem2/portfolio.html", context )