from rest_framework import permissions


class SelfAndAdminPermissionsCustom(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        if request.user.is_authenticated and obj.id == request.user.id:
            return True


class AdminPermissionsCustom(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
