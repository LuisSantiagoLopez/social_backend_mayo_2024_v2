from rest_framework import viewsets
from .models import Antro, MenuItem, Review
from .serializers import AntroSerializer, MenuItemSerializer, ReviewSerializer
from .permissions import IsAntroOwnerOrReadOnly, IsMenuItemAntroOwnerOrReadOnly, IsReviewOwnerOrReadOnly

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.gis.db.models.functions import Distance
from rest_framework import status
from django.contrib.gis.geos import Point

class AntroViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAntroOwnerOrReadOnly,)
    serializer_class = AntroSerializer

    def get_queryset(self):
        return Antro.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class MenuItemViewSet(viewsets.ModelViewSet):
    permission_classes = (IsMenuItemAntroOwnerOrReadOnly,)
    serializer_class = MenuItemSerializer

    def get_queryset(self):
        return MenuItem.objects.filter(antro__user=self.request.user)

    def perform_create(self, serializer):
        serializer.save()

class ReviewViewSet(viewsets.ModelViewSet):
    permission_classes = (IsReviewOwnerOrReadOnly,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

@api_view(['GET'])
def antros_close(request):
    try:
        longitude = float(request.query_params.get('longitude'))
        latitude = float(request.query_params.get('latitude'))
        user_location = Point(longitude, latitude, srid=4326)
    except (TypeError, ValueError):
        return Response({"error": "Invalid or missing latitude/longitude"}, status=status.HTTP_400_BAD_REQUEST)

    queryset = Antro.objects.annotate(distance=Distance('location', user_location)).order_by('distance')[:10]
    serializer = AntroSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def antros_relevant(request):
    user = request.user
    if user.is_authenticated and hasattr(user, 'antro_category_preference'):
        queryset = Antro.objects.filter(category=user.antro_category_preference)
    else:
        queryset = Antro.objects.none()
    
    serializer = AntroSerializer(queryset, many=True)
    return Response(serializer.data)