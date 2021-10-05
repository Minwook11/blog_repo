from django.db import models

class Case(models.Model):
    name = models.CharField(max_length=200)
    code = models.IntegerField()

class Level(models.Model):
    number = models.IntegerField()
    level = models.TextField()

class Complex(models.Model):
    case = models.ForeignKey('Case', on_delete = models.CASCADE)
    level = models.ForeignKey('Level', on_delete = models.CASCADE)
    key_1 = models.IntegerField()
    key_2 = models.IntegerField()
