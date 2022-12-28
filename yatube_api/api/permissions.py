from rest_framework import permissions


class AuthorPermission(permissions.BasePermission):
    """"Разрешения для автора полные, иначе только чтение."""
    def has_object_permission(self, request, view, obj):
        return(
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user)
