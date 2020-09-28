from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include
from game import urls
from game import views

from . import views

urlpatterns = [
	path('', views.input),
]
