from rest_framework import viewsets
from schoolapi.models import Student
from schoolapi.serializer import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer