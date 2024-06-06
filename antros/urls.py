from rest_framework.routers import SimpleRouter
from django.urls import path, include

from .views import AntroViewSet, MenuItemViewSet, ReviewViewSet, antros_close, antros_relevant

router = SimpleRouter()
router.register('antros-list', AntroViewSet)
router.register('menu-items', MenuItemViewSet, basename='menuitem')
router.register('reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('antros/close/', antros_close, name='antros-close'),
    path('antros/relevant/', antros_relevant, name='antros-relevant'),
]