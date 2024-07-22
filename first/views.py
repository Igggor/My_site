from django.shortcuts import render
import datetime

# Create your views here.

def index(request):
    context = {}
    return render(request, 'index.html', context)

def projects(request):
    context = {}
    return render(request, 'projects.html', context)