from django.shortcuts import render, redirect

from . import models, forms

def index(req):
	games = models.Game.objects.all()
	return render(req,'crud1/index.html', {
		'data' : games,
		})

def input(req):
	form_input = forms.TaskForm()

	if req.POST:
		form_input = forms.TaskForm(req.POST)

		if form_input.is_valid():
			form_input.save()
		return redirect('/crud1')

	games = models.Game.objects.all()
	return render(req,'crud1/input.html', {
		'data' : games,
		'form' : form_input,
		})		
	
def detail(req, id):
	games = models.Game.objects.filter(pk=id).first()
	return render(req, 'crud1/detail.html', {
		'data' : games,
		})

def delete(req, id):
	models.Game.objects.filter(pk=id).delete()
	return redirect('/crud1')

def edit(req, id):
	if req.POST:
		models.Game.objects.filter(pk=id).update(
			name=req.POST['name'],
			genre=req.POST['genre'],
			year=req.POST['year'],
			dev=req.POST['dev'])
		return redirect('/crud1')

	games = models.Game.objects.filter(pk=id).first()
	return render(req, 'crud1/edit.html', {
		'data' : games,
		})

# def index(req):
# 	crud1 = models.Menu.objects.all()
# 	return render(req,'crud1/index.html', {
# 		'data' : crud1,
# 		})
