from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from blog.models import Post
from django.contrib.auth.models import User


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
    userfirst = User.objects.all()
    userfilter = User.objects.filter(username="emmwee").first()
    userid = userfilter.id
    user  = User.objects.get(id=1 )
    # Post1 = Post(title="Test",content = "first test",author = user)
    # Post1.save()
    all_post = Post.objects.all()
    # user_post = user.post_set()
    user_post = user.post_set.all()
    # user_post_create = user.post_set.create(title= "user create",content = "user create post")
    # user_post_create.save()
    # get user with that post
    context = {
        'posts': user_post,
        'title' : userfilter,
    }
    return render(request, 'blog/home.html', context)
    # return HttpResponse("Home page")

def about(request):
    return render(request, 'blog/about.html')

    # return HttpResponse("about")
