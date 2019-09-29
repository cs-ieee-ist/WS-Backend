
from .entities import Student
import json

class CreateStudentSerializer:

	def __init__(self, request):
		self.request = request

	def requestSerializer(self):
		print("##############################################")
		print(f'TYPE: {type(self.request.data)}, REQUEST: {self.request.data}')
		print("##############################################")
		data = json.loads(self.request.data[0])
		print(data)
		name = data.get('name')
		age  = data.get('age')
		return Student(name, int(age))

	def responseSerializer(self):
		return 'User created successfully'

	def validate(self):
		return True