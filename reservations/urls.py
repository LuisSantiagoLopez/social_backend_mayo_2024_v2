from rest_framework.routers import SimpleRouter
from django.urls import path, include

from .views import ReservationViewSet, ReservationItemViewSet

router = SimpleRouter()
router.register('reservations', ReservationViewSet, basename='reservations')
router.register('reservations-menu-item', ReservationItemViewSet, basename='reservation-menu-item')

urlpatterns = [
    path('', include(router.urls)),
]