from rest_framework import viewsets
from .models import Employee
from .serializer import EmployeeSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    #Exibe todos os alunos
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

