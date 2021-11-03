from rest_framework import serializers
from schoolapi.models import Student

class StudentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Student
    fields = ['id', 'name', 'email', 'dateOfBirth']