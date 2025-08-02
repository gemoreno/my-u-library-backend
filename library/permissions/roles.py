from rest_framework.permissions import BasePermission, IsAdminUser

class IsStudent(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'student'


class IsLibrarian(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'librarian'
    
class IsAdminOrLibrarian(BasePermission):
    def has_permission(self, request, view):
        is_admin = IsAdminUser().has_permission(request, view)
        is_librarian = request.user.is_authenticated and request.user.role == "librarian"
        return is_admin or is_librarian
