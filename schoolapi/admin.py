from django.contrib import admin
from schoolapi.models import Student

class Students(admin.ModelAdmin): 
  list_display = ('id', 'name', 'email', 'dateOfBirth')
  list_display_links = ('id', 'name')
  search_fields = ('name', )

admin.site.register(Student, Students)