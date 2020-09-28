from django.shortcuts import render, redirect

from . import models, forms

def index(req):
	form_input = forms.TaskForm()

	if req.POST:
		form_input = forms.TaskForm(req.POST)

		if form_input.is_valid():
			form_input.save()
		return redirect('/')

	games = models.Task.objects.all()
	return render(req,'game/index.html', {
		'data' : games,
		'form' : form_input,
		})
	
def detail(req, id):
	#form_input = forms.TaskForm()

	games = models.Task.objects.filter(pk=id).first()
	return render(req, 'game/detail.html', {
		'data' : games,
	#	'form' : form_input,
		})

def delete(req, id):
	models.Task.objects.filter(pk=id).delete()
	return redirect('/')

def edit(req, id):
	if req.POST:
		models.Task.objects.filter(pk=id).update(
			name=req.POST['name'],
			description=req.POST['description'])
		return redirect('/')
	# form_input = forms.TaskForm()

	# if req.POST:
	# 	form_input = forms.TaskForm(req.POST)

	# 	if form_input.is_valid():
	# 		form_input.save()
	# 	return redirect('/')

	games = models.Task.objects.filter(pk=id).first()
	return render(req, 'game/edit.html', {
		'data' : games,
		})
