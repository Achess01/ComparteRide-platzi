""" Circles urls """
#Django
from django.urls import path, include

# Django REST Framework
from rest_framework.routers import DefaultRouter

#views
from .views import circles as circle_views
from .views import MembershipViewSet

router = DefaultRouter()
router.register(r'circles', circle_views.CircleViewSet, basename='circle')
router.register(
    r'circles/(?P<slug_name>[-a-zA-Z0-0_]+)/members',
    MembershipViewSet,
    basename='membership'
)


urlpatterns = [
    path('', include(router.urls))
]
