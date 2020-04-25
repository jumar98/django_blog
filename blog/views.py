from django.shortcuts import HttpResponse, render

# Create your views here.


def hello_world(request):
    return HttpResponse('Hello world')
