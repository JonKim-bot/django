from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]

def home(request):
    context = {
        'posts': posts,
        'title' : 'asd',
    }
    return render(request, 'blog/home.html', context)
    # return HttpResponse("Home page")

def about(request):
    return render(request, 'blog/about.html')

    # return HttpResponse("about")
