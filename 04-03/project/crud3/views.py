from django.shortcuts import render,redirect

from . import models, forms
# Create your views here.
def index(req):
	meal = models.Meal.objects.all()
	return render(req, 'crud3/index.html', {
		'data' : meal,
		})

def input(req):
	form_input = forms.TaskForm()

	if req.POST:
		form_input = forms.TaskForm(req.POST)

		if form_input.is_valid():
			form_input.save()
		return redirect('/crud3')

	meal = models.Meal.objects.all()
	return render(req, 'crud3/input.html', {
		'data' : meal,
		'form' : form_input,
		})

def detail(req, id):
	meal = models.Meal.objects.filter(pk=id).first()
	return render(req, 'crud3/detail.html', {
		'data' : meal,
		})

def edit(req, id):
	if req.POST:
		models.Meal.objects.filter(pk=id).update(
			merk = req.POST['merk'],
			type_meal = req.POST['type_meal'],
			price = req.POST['price'])
		return redirect('/crud3')

	meal = models.Meal.objects.filter(pk=id).first()
	return render(req, 'crud3/edit.html', {
		'data' : meal,
		})

def delete(req, id):
	models.Meal.objects.filter(pk=id).delete()
	return redirect('/crud3')