from rest_framework import serializers
from .models import Reservation, ReservationItem

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id', 'antro', 'user', 'cost', 'created_at']

class ReservationItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservationItem
        fields = ['id', 'reservation', 'menu_item', 'quantity']
