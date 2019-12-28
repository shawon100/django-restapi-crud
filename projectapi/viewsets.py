from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework import filters 
from django_filters.rest_framework import DjangoFilterBackend

class EmployeeViewset(viewsets.ModelViewSet):
    queryset=models.Employee.objects.all()
    serializer_class=serializers.EmployeeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['emp_code','mobile']
