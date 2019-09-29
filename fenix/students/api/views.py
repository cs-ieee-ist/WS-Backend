from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import CreateStudentSerializer, GetStudentSerializer, GetStudentsSerializer

from students.models import StudentModel
from students.student import Student, create_student, get_students, get_student


class StudentView(APIView):

	def get(self, request):
		student_name = GetStudentSerializer(request).requestSerializer()
		try:
			student = get_student(student_name)
		except Exception as e:
			return GetStudentSerializer(request).errorSerializer(e)
		return GetStudentSerializer(request).responseSerializer(student)

	def post(self, request):
		student = CreateStudentSerializer(request).requestSerializer()
		create_student(student)
		return CreateStudentSerializer(request).responseSerializer()

class StudentsView(APIView):

	def get(self, request):
		GetStudentsSerializer(request).requestSerializer()
		students = get_students()
		return GetStudentsSerializer(request).responseSerializer(students)
