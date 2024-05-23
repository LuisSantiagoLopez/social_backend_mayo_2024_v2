from rest_framework import viewsets
from .models import Reservation, ReservationItem
from .serializers import ReservationSerializer, ReservationItemSerializer

from .permissions import IsReservationOwnerOrReadOnly, IsReservationItemOwnerOrAntroOwnerOrReadOnly

class ReservationViewSet(viewsets.ModelViewSet):
    permission_classes = (IsReservationOwnerOrReadOnly,)
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class ReservationItemViewSet(viewsets.ModelViewSet):
    permission_classes = (IsReservationItemOwnerOrAntroOwnerOrReadOnly,)
    queryset = ReservationItem.objects.all()
    serializer_class = ReservationItemSerializer
