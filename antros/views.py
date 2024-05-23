from rest_framework import viewsets
from .models import Antro, MenuItem, Review
from .serializers import AntroSerializer, MenuItemSerializer, ReviewSerializer
from .permissions import IsAntroOwnerOrReadOnly, IsMenuItemAntroOwnerOrReadOnly, IsReviewOwnerOrReadOnly

class AntroViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAntroOwnerOrReadOnly,)
    queryset = Antro.objects.all()
    serializer_class = AntroSerializer

    def get_queryset(self):
        return Antro.objects.filter(user=self.request.user)

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
