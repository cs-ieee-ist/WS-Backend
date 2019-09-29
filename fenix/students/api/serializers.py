
from students.student import Student
from rest_framework.response import Response

class CreateStudentSerializer:

	def __init__(self, request):
		self.request = request

	def requestSerializer(self):
		data = self.request.data.dict()
		name = data.get('name')
		age  = data.get('age')
		return Student(name, int(age))

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
