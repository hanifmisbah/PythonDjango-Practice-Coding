from django.shortcuts import render

from . import models

def index(request):
	if request.POST:
		models.Task.objects.create(name=request.POST['name'])

	tasks = models.Task.objects.all()
	return render(request, 'task/index.html', {
		'data' : tasks,
		})

# def delete(request):
# 	if request.POST:
# 		models.Delete.objects.delete(delete=request.POST['id'])

# 	tasks = models.Delete.objects.all()
# 	return render(request, 'task/index.html', {
# 		'data' : tasks,
# 		})

# def delete(request):
#     query = People.objects.get(pk=id)
#     query.delete()
#     return HttpResponse("Deleted!")