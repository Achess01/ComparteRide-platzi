"""  User permissions """

# Django REST Framework
from rest_framework.permissions import BasePermission


class IsAccountOwner(BasePermission):
    """ Allow access only to objects by the requestin user """

    def has_object_permission(self, request, view, obj):
        return request.user == obj
