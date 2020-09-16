from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from Cerveza.models import cerveza

def index(request):
    context = {
        'titulo' : 'Lobby',
        'texto' : 'Bienvenido'
    }
    return render(request,'cerveza.html', context)

def cerveza_list(request):
    context = {
        'cerveza_list': cerveza.objects.all()
    }
    return render(request,'cerveza_list.html', context)

def cerveza_detail(request,pk):

    print("user: ",request.user)
    print("get: ",request.GET)
    print("metod: ",request.method)
    print("ajax: ",request.is_ajax())

    context = {
        'nombre':cerveza.objects.get(pk=pk)
    }
    return render(request,'cerveza_details.html', context)