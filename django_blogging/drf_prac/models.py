from django.db import models

class Practice(models.Model):
	attr_1 = models.IntegerField()
	attr_2 = models.IntegerField()
	attr_3 = models.IntegerField()

	def __str__(self):
		return self.title
