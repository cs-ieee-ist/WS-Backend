
from .models import StudentModel

class Student:

	def __init__(self, name, age):
		self.name = name
		self.age = age


def create_student(student: Student):
	try:
		st_model = StudentModel(name=student.name, age=student.age)
		st_model.save()
	except Exception as e:
		print(e)
		raise e

def get_students():
	try:
		students = [Student(s.name, s.age) for s in StudentModel.objects.all()]
		return students
	except Exception as e:
		print(e)
		raise e

def get_student(name: str) -> Student:
	try:
		student_list = StudentModel.objects.get(name=name)
		return Student(student.name, student.age)
	except Exception as e:
		print(e)
		raise e