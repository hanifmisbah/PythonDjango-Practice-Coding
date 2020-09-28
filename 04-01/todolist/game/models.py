from django.db import models

class Game(models.Model):
	name = models.TextField(default='')
	# snps = models.TextField(default='')
	genre = models.TextField(default='')
	year = models.TextField(default='')
	dev = models.TextField(default='')

class Task(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField(max_length=500)