from django.shortcuts import HttpResponse

# Create your views here.

def hello_view(request):

    return HttpResponse("Hello! It's my project")

def currentdate_view(request):

    return HttpResponse("17.11.2023")

def goodby_view(request):

    return HttpResponse("Goodby user!")
