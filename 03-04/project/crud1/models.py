from django.db import models

# from menu.models import Menu
class Game(models.Model):
	name = models.TextField(default='')
	genre = models.TextField(default='')
	year = models.TextField(default='')
	dev = models.TextField(default='')
