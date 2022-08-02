""" Invitation permissions """

# Permissions
from rest_framework.permissions import BasePermission




class IsSelfMember(BasePermission):
    """ Allow access only to the owner invitations """

    def has_permission(self, request, view):
        obj = view.get_object()
        print(obj.user)
        print(request.user)
        return request.user == obj.user

