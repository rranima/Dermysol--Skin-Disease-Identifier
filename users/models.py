from django.db import models

# Create your models here.
class Disease(models.Model):
	name = models.CharField(max_length=500)
	description = models.TextField()

	def __str__(self):
		return self.name