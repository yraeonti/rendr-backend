from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from core import models
from core import serializers
from rest_framework.permissions import IsAuthenticated, IsAdminUser
import random
from core.permissions import IsOwner, IsEmployeeOwner
from parser.parser import parse_file
from pathlib import Path
from django.db.models import Q

# Create your views here.

class RequestCategory(generics.ListAPIView):
    queryset = models.RequestCategory.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.RequestCategorySerializer


# views for the employees functionality
class Employees(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.EmployeesSerializer

    def get_queryset(self):
        user = self.request.user
        data = models.Employee.objects.filter(company=user)
        return data
    
    def perform_create(self, serializer):
        serializer.save(company=self.request.user)

class BulkCreateEmployee(generics.GenericAPIView):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeesSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def post(self, *args, **kwargs):
        serializer = self.get_serializer(data=self.request.data, many=True)
        if serializer.is_valid() is False:
            return Response(data=serializer.errors, status=400)
        print(serializer.validated_data)
        data = [models.Employee(**item, company_id=self.request.user.id) for item in serializer.validated_data]
        models.Employee.objects.bulk_create(data)
        return Response(data={"message": "Employees created"}, status=201)

    
class SingleEmployee(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeesSerializer
    permission_classes = [IsAuthenticated, IsEmployeeOwner]

class SearchEmployees(generics.ListAPIView):
    serializer_class = serializers.EmployeesSerializer
    permission_classes = [IsAuthenticated]
    
    def list(self, request, *args, **kwargs):
        data = self.get_queryset()
        obj = data
        if 'search' in request.query_params:
            obj = data.filter(Q(name__contains=request.query_params['search']) | Q(email__contains=request.query_params['search']))
        serializer = self.get_serializer(obj, many=True)
        return Response(serializer.data)
    
    def get_queryset(self):
        user = self.request.user
        data = models.Employee.objects.filter(company=user)
        return data





# views for the request functionality
class Requests(generics.ListCreateAPIView):
    serializer_class = serializers.RequestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        data = models.Request.objects.filter(user=user)
        return data


    def perform_create(self, serializer):
        id = 'RQ' + str(random.randint(10000, 99999))
        serializer.save(request_id=id, user=self.request.user)

class SingleRequest(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Request.objects.all()
    serializer_class = serializers.RequestSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class ParseRequestFile(generics.GenericAPIView):
    serializer_class = serializers.ParseRequestFileSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(self, data=request.FILES)
        if serializer.is_valid() is False:
            return Response(data=serializer.errors, status=400)
        print(serializer.validated_data['file'])
        file = serializer.validated_data['file']

        ext = file.name.split(".")[1]

        # curr_dir = Path.cwd()

        # file_path = f"{curr_dir}/core/tmp/{request.user.id}.{ext}"

        # print(file_path)

        data = parse_file(file, ext)

        return Response(data=data, status=200)
    
class ParseBulkEmployeesFile(generics.GenericAPIView):
    serializer_class = serializers.ParseBulkEmployeesFileSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(self, data=request.FILES)
        if serializer.is_valid() is False:
            return Response(data=serializer.errors, status=400)
        file = serializer.validated_data['file']

        ext = file.name.split(".")[1]

        data = parse_file(file, ext)

        serializerEmployee = serializers.EmployeesSerializer(data=data, many=True)
        if serializerEmployee.is_valid() is False:
            return Response(data=serializerEmployee.errors, status=400)
        
        employees_data = [models.Employee(**item, company_id=self.request.user.id) for item in serializerEmployee.validated_data]
        
        models.Employee.objects.bulk_create(employees_data)
        return Response(data={"message": "Employees created"}, status=201)




        
