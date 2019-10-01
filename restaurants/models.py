from django.db import models

# Create your models here.
class Restaurant(models.Model):
	name = models.CharField(max_length=105)
	description = models.CharField(max_length=105)
	opening_time = models.CharField(max_length=5)
	closing_time = models.CharField(max_length=5)

	def __str__(self):
		return self.name