from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    edit_methods = ("PUT", "PATCH", "DELETE")

    def has_permission(self, request, view):
        return bool(request.method in permissions.SAFE_METHODS or
                    request.method not in self.edit_methods or
                    request.user and request.user.is_staff)

    def has_object_permission(self, request, view, obj):
        return bool(request.method in permissions.SAFE_METHODS or
                    request.method not in self.edit_methods or
                    request.user and request.user.is_staff)
