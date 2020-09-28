from django.db import models

class Task(models.Model):
	name = models.TextField()

# class Delete(models.Model):
# 	name = models.Delete()