from rest_framework import serializers
from .models import Antro, MenuItem, Review
from django.contrib.gis.geos import Point


class AntroSerializer(serializers.ModelSerializer):
    latitude = serializers.FloatField(write_only=True)
    longitude = serializers.FloatField(write_only=True)

    class Meta:
        model = Antro
        fields = ['id', 'user', 'image', 'name', 'description', 'contact', 'approved', 'category', 'cost', 'latitude', 'longitude']

    def create(self, validated_data):
        latitude = validated_data.pop('latitude')
        longitude = validated_data.pop('longitude')
        validated_data['location'] = Point(longitude, latitude, srid=4326)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        latitude = validated_data.pop('latitude', None)
        longitude = validated_data.pop('longitude', None)
        if latitude is not None and longitude is not None:
            instance.location = Point(longitude, latitude, srid=4326)
        return super().update(instance, validated_data)

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'image', 'name', 'description', 'category', 'price', 'antro']

    def validate_antro(self, value):
        request = self.context['request']
        if not Antro.objects.filter(id=value.id, user=request.user).exists():
            raise serializers.ValidationError("You can only add menu items to your own antros.")
        return value

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'user', 'rating', 'comment', 'antro']
