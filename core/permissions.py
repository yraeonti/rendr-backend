from rest_framework import permissions

class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
    

class IsEmployeeOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.company == request.user