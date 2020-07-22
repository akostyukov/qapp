from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tobacco

# Create your views here.
def index(request):
    return render(request, 'ds/index.html', {"tobacco_list": Tobacco.objects.all()})

def create(request):
    Tobacco.objects.create(tobacco_name=request.POST['tobacco'])
    return redirect('ds:index')

def delete(request, tobacco_id):
    Tobacco.objects.get(id=tobacco_id).delete()
    return redirect('ds:index')