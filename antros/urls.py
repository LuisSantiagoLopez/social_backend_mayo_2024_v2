from rest_framework.routers import SimpleRouter
from django.urls import path, include

from .views import AntroViewSet, MenuItemViewSet, ReviewViewSet

router = SimpleRouter()
router.register('antros-list', AntroViewSet)
router.register('menu-items', MenuItemViewSet, basename='menuitem')
router.register('reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
]