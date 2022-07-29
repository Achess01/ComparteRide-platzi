""" Circle views. """

# Django REST framework
from rest_framework import viewsets

#Serializers
from cride.circles.serializers import CircleModelSerializer

#Modesl
from cride.circles.models import Circle

class CircleViewSet(viewsets.ModelViewSet):
    """ Circle view set """
    queryset = Circle.objects.all()
    serializer_class = CircleModelSerializer
