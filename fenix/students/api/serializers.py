from django.http import JsonResponse

from students.student import Student
from rest_framework.response import Response
from rest_framework import status


class CreateStudentSerializer:

	def __init__(self, request):
		self.request = request

	def requestSerializer(self):
		data = self.request.data
		name = data.get('name')
		age  = data.get('age')
		print(name)
		print(age)
		return Student(name, age)

	def responseSerializer(self):
		return Response('User created successfully')

	def errorSerializer(self, error):
		return Response(str(error), status=status.HTTP_400_BAD_REQUEST)



class GetStudentSerializer:

	def __init__(self, request):
		self.request = request

	def requestSerializer(self):
		# data = self.request.data.dict()
		return "Vasco"

	def responseSerializer(self, student):
		student_dict = {"name": student.name, "age": student.age}
		return Response(str(student_dict))

	def errorSerializer(self, error):
		return Response(str(error), status=status.HTTP_400_BAD_REQUEST)



class GetStudentsSerializer:

	def __init__(self, request):
		self.request = request

	def requestSerializer(self):
		pass

	def responseSerializer(self, students):
		students_list = []
		for s in students:
			students_list.append({"name": s.name, "age": s.age})
		response = str(students_list)
		return Response(response)

	def errorSerializer(self, error):
		return Response(str(error), status=status.HTTP_400_BAD_REQUEST)
