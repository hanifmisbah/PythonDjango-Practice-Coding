from django.db import models

class Task(models.Model):
	name = models.TextField(default='')
	status = models.TextField(default='Lola')