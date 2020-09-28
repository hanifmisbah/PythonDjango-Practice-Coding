from django.shortcuts import render, redirect

from . import models, forms
# Create your views here.
def index(req):
	coffe = models.Coffe.objects.all()
	return render(req, 'crud2/index.html', {
		'data' : coffe,
		})

def input(req):
	form_input = forms.TaskForm()

	if req.POST:
		form_input = forms.TaskForm(req.POST)

		if form_input.is_valid():
			form_input.save()
		return redirect('/crud2')

	coffe = models.Coffe.objects.all()
	return render(req, 'crud2/input.html', {
		'data' : coffe,
		'form' : form_input,
		})

def detail(req, id):
	coffe = models.Coffe.objects.filter(pk=id).first()
	return render(req, 'crud2/detail.html', {
		'data' : coffe,
		})

def delete(req, id):
	models.Coffe.objects.filter(pk=id).delete()
	return redirect('/crud2')


def edit(req, id):
	if req.POST:
		models.Coffe.objects.filter(pk=id).update(
			merk_coffe=req.POST['merk_coffe'],
			type_coffe=req.POST['type_coffe'],
			roasteds=req.POST['roasteds'],
			process=req.POST['process'],
			altitudes=req.POST['altitudes'])
		return redirect('/crud2')

	coffe = models.Coffe.objects.filter(pk=id).first()
	return render(req, 'crud2/edit.html', {
		'data' : coffe,
		})
