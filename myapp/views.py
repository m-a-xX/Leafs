from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def credits(request):
    return render(request, 'credits.html')

def leafs(request):
    return render(request, 'leafs.html')

def qcm(request):
    return render(request, 'qcm.html')