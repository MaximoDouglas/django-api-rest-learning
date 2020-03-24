"""pontos_turisticos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from tourist_attractions.api.viewsets import TouristAttractionViewSet
from shows.api.viewsets import ShowViewSet
from adresses.api.viewsets import AdressViewSet
from comments.api.viewsets import CommentViewSet
from ratings.api.viewsets import RatingViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'pontosturisticos', TouristAttractionViewSet, basename='TouristAttraction')
router.register(r'atracoes', ShowViewSet)
router.register(r'enderecos', AdressViewSet)
router.register(r'comentarios', CommentViewSet)
router.register(r'avaliacoes', RatingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_auth_token),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)