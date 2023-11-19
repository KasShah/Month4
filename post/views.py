from django.shortcuts import HttpResponse
import datetime

# Create your views here.

def hello_view(request):

    return HttpResponse("Hello! It's my project")

def currentdate_view(request):
    now = datetime.datetime.now()
    date_string = now.strftime("%Y-%m-%d")
    return HttpResponse(date_string)

def goodby_view(request):

    return HttpResponse("Goodby user!")
