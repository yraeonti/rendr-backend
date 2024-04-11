from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from core import models
from core import serializers
from rest_framework.permissions import IsAuthenticated, IsAdminUser
import random
from core.permissions import IsOwner

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
        data = models.Employee.objects.filter(user=user)
        return data
    
    def perform_create(self, serializer):
        serializer.save(company=self.request.user)

class BulkCreateEmployee(generics.GenericAPIView):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeesSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def post(self, *args, **kwargs):
        serializer = self.get_serializer(self, data=self.request.data, many=True)
        if serializer.is_valid() is False:
            return Response(data=serializer.errors, status=400)
        print(serializer.validated_data)
        data = [models.Employee(**item, company_id=self.request.user.id) for item in serializer.validated_data]
        models.Employee.objects.bulk_create(data)
        return Response(data={"message": "Employees created"}, status=201)

    
class SingleEmployee(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeesSerializer
    permission_classes = [IsAuthenticated, IsOwner]


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



        