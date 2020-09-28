from django.db import models

# from menu.models import Menu
class Game(models.Model):
	name = models.CharField(max_length=50)
	genre = models.CharField(max_length=50)
	year = models.CharField(max_length=20)
	dev = models.CharField(max_length=50)
