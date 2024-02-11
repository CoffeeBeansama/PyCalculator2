from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def helloWorld(request):
    return HttpResponse("Hello World")

def calculator(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render({},request))

