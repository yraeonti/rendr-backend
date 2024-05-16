
from rest_framework import serializers
from core.models import (
    Employee,
    RequestCategory,
    Request
)


class EmployeesSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Employee
        fields = ['id', 'name', 'email', 'role']

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

class ParseRequestFileSerializer(serializers.Serializer):
    file = serializers.FileField()

    def validate_file(self, value):
        ext = value.name.split(".")[1]
        if ext not in ('csv', 'xlsx', 'xls'):
            raise serializers.ValidationError("Invalid File type")
        return value
    

class ParseBulkEmployeesFileSerializer(ParseRequestFileSerializer):
    pass
