from django.db import models
from typing import List
from .student import Student

# Create your models here.

class StudentModel(models.Model):
	name  = models.CharField(max_length=100, blank=True)
	age   = models.IntegerField()

	def __str__(self):
		return f'Hi! My name is {self.name} and I am {self.age}'

def create_student(student: Student):
	try:
		st_model = StudentModel(name=student.name, age=student.age)
		st_model.save()
	except Exception as e:
		print(e)
		raise e

def get_students() -> List[Student]:
	try:
		students = [Student(s.name, s.age) for s in StudentModel.objects.all()]
		return students
	except Exception as e:
		print(e)
		raise e

def get_student(name: str) -> Student:
	try:
		student = StudentModel.objects.get(name=name)
		return Student(student.name, student.age)
	except Exception as e:
		print(e)
		raise e

def update_student(name: str, student_updates: Student) -> Student:
	try:
		student = StudentModel.objects.get(name=name)
		student.name = student_updates.name
		student.age = student_updates.age
		student.save()
		return Student(student.name, student.age)
	except Exception as e:
		print(e)
		raise e
