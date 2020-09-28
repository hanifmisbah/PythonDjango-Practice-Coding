from django.db import models

# Create your models here.
class Meal(models.Model):
	merk = models.CharField(max_length=50)
	type_meal = models.CharField(max_length=50)
	price = models.CharField(max_length=50)