"""Fil that contains views use in urls"""
from django.shortcuts import render

# Create your views here.

def index(request):
    """Homepage view"""
    return render(request, 'index.html')

def credits(request):
    """Legal mentions view"""
    return render(request, 'credits.html')

def leafs(request):
    """Leafs view"""
    return render(request, 'leafs.html')

def qcm(request):
    """QCM view"""
    return render(request, 'qcm.html')
