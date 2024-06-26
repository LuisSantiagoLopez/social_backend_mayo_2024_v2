from django.contrib.auth import get_user_model
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'birthdate']

class CustomRegisterSerializer(RegisterSerializer):
    birthdate = serializers.DateField(required=False)
    antro_category_preference = serializers.CharField(required=False, max_length=100)

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict['birthdate'] = self.validated_data.get('birthdate', None)
        data_dict['antro_category_preference'] = self.validated_data.get('antro_category_preference', None)
        return data_dict

    def save(self, request):
        user = super().save(request)
        user.birthdate = self.validated_data.get('birthdate', None)
        user.antro_category_preference = self.validated_data.get('antro_category_preference', None)
        user.save()
        return user
