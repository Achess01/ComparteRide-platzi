""" Profile serializers """

# Django REST Framework
from rest_framework import serializers


# Models
from cride.users.models import Profile


class ProfileModelSerializer(serializers.ModelSerializer):
    """ Profile model serializer """


    class Meta:
        """ Metas class """
        model = Profile
        fields = (
            'picture',
            'biography',
            'rides_taken',
            'rides_offered',
            'reputation'
        )
        read_only_fields = (
            'rides_taken',
            'rides_offered',
            'reputation'
            )
