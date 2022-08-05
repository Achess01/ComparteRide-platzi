""" Rides permissions """

# Django REST framework
from rest_framework.permissions import BasePermission


class IsRideOwner(BasePermission):
    """ Verify  requesting user is the ride create"""

    def has_object_permission(self, request, view, obj):
        """ Verify  requesting user is the ride creator"""
        return request.user == obj.offered_by


class IsNotRideOwner(BasePermission):
    """ Verify  requesting user is not the ride creator"""

    def has_object_permission(self, request, view, obj):
        """ Verify  requesting user is not the ride creator"""
        return request.user != obj.offered_by
