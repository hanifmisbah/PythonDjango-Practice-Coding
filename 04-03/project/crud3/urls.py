from django.urls import path

from . import views

urlpatterns = [
	path('input/', views.input),
	path('', views.index),
	path('<id>/', views.detail),
	path('<id>/edit', views.edit),
	path('<id>/delete', views.delete),
]