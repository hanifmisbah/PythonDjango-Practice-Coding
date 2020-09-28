from django.shortcuts import render, redirect

from . import models


def index(request):
	if request.POST:
		models.Task.objects.create(name=request.POST['name'])
		return redirect('/')

	tasks = models.Task.objects.all()
	return render(request, 'task/index.html', {
		'data' : tasks,
		})


def detail(request, id):
	task = models.Task.objects.filter(pk=id).first()
	return render(request, 'task/detail.html', {
		'data' : task,
		})


def delete(request, id):
	task = models.Task.objects.filter(pk=id).delete()
	return redirect('/')

def edit(request, id):
	if request.POST:
		models.Task.objects.filter(pk=id).update(name=request.POST['name'])
		return redirect('/')

	task = models.Task.objects.filter(pk=id).first()
	return render(request, 'task/edit.html', {
			'data' : task,
			})

