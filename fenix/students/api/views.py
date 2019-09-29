from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import CreateStudentSerializer, GetStudentsSerializer

from students.db.models import StudentModel
from students.entities import Student

class StudentView(APIView):

	def get(self, request):
		students = get_students()
		return GetStudentsSerializer(request).responseSerializer(students)

	def post(self, request):
		student = CreateStudentSerializer(request).requestSerializer()
		create_student(student)
		return CreateStudentSerializer(request).responseSerializer()



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
		student = StudentModel(name=name)
		return Student(student.name, student.age)
	except Exception as e:
		print(e)
		raise e