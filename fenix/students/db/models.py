from django.db import models

# Create your models here.

class StudentModel(models.Model):
	name  = models.CharField(max_length=100, null=True, blank=True)
	age   = models.IntegerField()
	email = models.CharField(max_length=100, null=True, blank=True)

	def __str__(self):
		return f'Hi! My name is {self.name} and I am {self.age}'
