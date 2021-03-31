from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index2(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def test2(request):
    return HttpResponse("test2")
