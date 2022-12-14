""" Rides urls """
#Django
from django.urls import path, include

# Django REST Framework
from rest_framework.routers import DefaultRouter

#views
from .views import rides as ride_views


router = DefaultRouter()
router.register(
    r'circles/(?P<slug_name>[-a-zA-Z0-0_]+)/rides',
    ride_views.RideViewSet,
    basename='ride'
)


urlpatterns = [
    path('', include(router.urls))
]
