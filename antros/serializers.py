from rest_framework import serializers
from .models import Antro, MenuItem, Review

class AntroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Antro
        fields = ['id', 'user', 'image', 'name', 'description', 'contact', 'approved', 'category', 'cost']

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
