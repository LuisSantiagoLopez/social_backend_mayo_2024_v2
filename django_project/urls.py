"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    # Admin page 
    path('admin/', admin.site.urls),

    # Applications
    path('antros/', include('antros.urls')),
    path('accounts/', include('accounts.urls')),
    path('reservations/', include('reservations.urls')),

    # Authentication and Documentation through 3rd party applications:
    
    path('api-auth/', include('rest_framework.urls')), # Login and Logout through /api-auth/login/ and /api-auth/logout/ for browsable API
    path('dj-rest-auth/', include('dj_rest_auth.urls')), # Login, Logout, Password Reset, Password Change, User Profile through /dj-rest-auth/login/, /dj-rest-auth/logout/, /dj-rest-auth/password/reset/, /dj-rest-auth/password/change/, /dj-rest-auth/user/ 
    path(
        'dj-rest-auth/registration/', 
        include('dj_rest_auth.registration.urls')
    ), # Register through /dj-rest-auth/registration/ and verify email through /dj-rest-auth/registration/account-confirm-email/<key>/ (not enabled)
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc',), 
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
