from rest_framework.routers import SimpleRouter
from django.urls import path, include

from .views import AntroViewSet, MenuItemViewSet, ReviewViewSet, antros_close, antros_relevant

router = SimpleRouter()
router.register('antros-list', AntroViewSet)
router.register('menu-items', MenuItemViewSet, basename='menuitem')
router.register('reviews', ReviewViewSet)

router.register('antros-close', antros_close)
router.register('antros-relevant', antros_relevant)

urlpatterns = [
    path('', include(router.urls)),
]