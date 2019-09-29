from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import CreateStudentSerializer

from .models import StudentModel
from .entities import Student

class StudentView(APIView):

	def get(self, request):
		students = StudentModel.objects.all()
		print("##############################################")
		print(students)
		print("##############################################")
		return Response({"students": "ola"})

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
