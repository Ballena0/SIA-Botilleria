from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def index(request):
    template = loader.get_template('base.html')
    context = {}
    return HttpResponse(template.render(context, request))

def productos(request):
    return HttpResponse("esta es otra vista, la de los productos")

def tipo_formato(request):
    return HttpResponse("Esta es la de los formatos")