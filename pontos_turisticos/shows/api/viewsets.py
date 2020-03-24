from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from shows.api.serializers import ShowSerializer
from shows.models import Show

class ShowViewSet(ModelViewSet):
    queryset         = Show.objects.all()
    serializer_class = ShowSerializer
    filter_backends  = (DjangoFilterBackend,)
    filter_fields    = ('name', 'description')