from django.contrib import admin
from django.urls import path, include
from schoolapi.views import StudentViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'students', StudentViewSet)

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', include(router.urls))
]
