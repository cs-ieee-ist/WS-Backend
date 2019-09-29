from django.urls import path

from .views import StudentView, StudentsView

urlpatterns = [
    path('student/', StudentView.as_view()),
    path('students/', StudentsView.as_view())
]
