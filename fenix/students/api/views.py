# Generic Views

# https://www.django-rest-framework.org/api-guide/generic-views/

from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Student

class StudentView(APIView):
	def get(self, request):
		students = Student.objects.all()
		return Response({"students": students})