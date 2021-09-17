from django.db import models

class Case(models.Model):
    name = models.CharField(max_length=200)
    code = models.IntegerField()
