from django.shortcuts import render, redirect

from . import models

def index(req):
	if req.POST:
		models.Game.objects.create(
			name=req.POST['name'],
			genre=req.POST['genre'],
			year=req.POST['year'],
			dev=req.POST['dev'])
		return redirect('/')

	games = models.Game.objects.all()
	return render(req,'game/index.html', {
		'data' : games,
		})
	
def detail(req, id):
	games = models.Game.objects.filter(pk=id).first()
	return render(req, 'game/detail.html', {
		'data' : games,
		})

def delete(req, id):
	models.Game.objects.filter(pk=id).delete()
	return redirect('/')

def edit(req, id):
	if req.POST:
		models.Game.objects.filter(pk=id).update(
			name=req.POST['name'],
			genre=req.POST['genre'],
			year=req.POST['year'],
			dev=req.POST['dev'])
		return redirect('/')

	games = models.Game.objects.filter(pk=id).first()
	return render(req, 'game/edit.html', {
		'data' : games,
		})
	
def input(req):
	if req.POST:
		models.Game.objects.create(
			name=req.POST['name'],
			genre=req.POST['genre'],
			year=req.POST['year'],
			dev=req.POST['dev'])
		return redirect('/')

	games = models.Game.objects.all()
	return render(req,'game/index.html', {
		'data' : games,
		})