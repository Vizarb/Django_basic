from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [   
    path('', views.index, name='index'),  # Home page
    path('test', views.test, name='index'),  # Home page

]
