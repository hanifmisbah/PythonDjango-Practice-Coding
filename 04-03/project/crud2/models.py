from django.db import models

# Create your models here.
class Coffe(models.Model):
	merk_coffe = models.CharField(max_length=50)
	type_coffe = models.CharField(max_length=50)
	roasteds = models.CharField(max_length=20)
	process = models.CharField(max_length=50)
	altitudes = models.CharField(max_length=50)