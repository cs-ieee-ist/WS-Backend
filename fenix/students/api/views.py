from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import CreateStudentSerializer, GetStudentSerializer, GetStudentsSerializer, UpdateStudentSerializer

from students.models import StudentModel, create_student, get_students, get_student, update_student
from students.student import Student


class StudentView(APIView):

	def get(self, request):
		ioSerializer = GetStudentSerializer(request)
		studentName = ioSerializer.requestSerializer()
		try:
			student = get_student(studentName)
		except Exception as e:
			return ioSerializer.errorSerializer(e)
		return ioSerializer.responseSerializer(student)

	def post(self, request):
		ioSerializer = CreateStudentSerializer(request)
		student = ioSerializer.requestSerializer()
		try:
			create_student(student)
		except Exception as e:
			return ioSerializer.errorSerializer(e)
		return ioSerializer.responseSerializer()

	def patch(self, request):
		ioSerializer = UpdateStudentSerializer(request)
		studentName, studentUpdates = ioSerializer.requestSerializer()
		try:
			student = update_student(studentName, studentUpdates)
		except Exception as e:
			return ioSerializer.errorSerializer(e)
		return ioSerializer.responseSerializer(student)

class StudentsView(APIView):

	def get(self, request):
		ioSerializer = GetStudentsSerializer(request)
		ioSerializer.requestSerializer()
		try:
			students = get_students()
		except Exception as e:
			return ioSerializer.errorSerializer(e)
		return ioSerializer.responseSerializer(students)
