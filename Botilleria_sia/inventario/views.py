from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from django.views.generic import CreateView, TemplateView
from django.http import JsonResponse
# Create your views here.

def index(TemplateView):
    template_name = 'index.html'
    return HttpResponse(template_name)

def productos(request):
    return HttpResponse("esta es otra vista, la de los productos")

def tipo_formato(request):
    return HttpResponse("Esta es la de los formatos")