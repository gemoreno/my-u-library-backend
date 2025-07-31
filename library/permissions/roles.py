from rest_framework.permissions import BasePermission

class IsLibrarian(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name="librarian").exists()

class IsStudent(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name="student").exists()
