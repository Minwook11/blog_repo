from django.db import models

class Practice(models.Model):
	attr_1 = models.IntegerField()
	attr_2 = models.IntegerField()
	attr_3 = models.IntegerField()

	def __str__(self):
		return self.title

class Nested(models.Model):
	date = models.DateTimeField(auto_now_add = True)
	nested_1 = models.CharField(max_length = 32)
	prac = models.ForeignKey(Practice, on_delete = models.CASCADE)

class Student(models.Model):
	name = models.CharField(max_length = 64)
	age  = models.IntegerField()
	grade = models.IntegerField()

class Lecture(models.Model):
	name = models.CharField(max_length = 256)
	length = models.IntegerField()
	is_compulsory = models.BooleanField()

class Enrolment(models.Model):
	student = models.ForeignKey(Student, on_delete = models.CASCADE)
	lecture = models.ForeignKey(Lecture, on_delete = models.CASCADE)

