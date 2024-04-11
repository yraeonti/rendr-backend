
from rest_framework import serializers
from core.models import (
    Employee,
    RequestCategory,
    Request
)


class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['name', 'email', 'role']

class RequestCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestCategory
        fields = ['id', 'item']

class RequestSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    request_category = serializers.SlugRelatedField(slug_field='id', queryset=RequestCategory.objects) 
    class Meta:
        model = Request
        fields = ['request_id', 'user', 'procure_items', 'approvals', 'status', 'created_at', 'request_category']