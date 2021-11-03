from django.db import models

class Student(models.Model):
  name = models.CharField(max_length = 30)
  email = models.EmailField()
  dateOfBirth = models.DateField()

  def __string__(self):
    return self.name