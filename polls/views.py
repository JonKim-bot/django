from django.http import HttpResponse
import time

def index(request):

    return HttpResponse("Hello, world. You're at the polls index.")

def test2(request):
    return HttpResponse("test2")