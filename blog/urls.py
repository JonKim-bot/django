from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('api_test', views.api_test, name='api_test'),

    path('about', views.about, name='blog-about'),
]