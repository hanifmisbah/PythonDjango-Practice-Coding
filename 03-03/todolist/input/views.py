from django.shortcuts import render

from game import models

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