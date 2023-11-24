from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    def has_permission(self, request, view):
        if view.action in ('update', 'partial_update', 'destroy'):
            return request.user == view.get_object().owner
        return True
