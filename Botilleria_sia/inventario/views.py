from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
# Create your views here.

def index(request):
    ##numbers = [int (i) for i in request.GET['numbers'].split(',')]
    ##sorteados= sorted(numbers)
    ##return JsonResponse(sorteados, safe=False)
    return HttpResponse("esta es la primera vista, donde aparecen productos y todo eso blaa bla")

def productos(request):
    return HttpResponse("esta es otra vista, la de los productos" )

def tipo_formato(request):
    return HttpResponse("Esta es la de los formatos")