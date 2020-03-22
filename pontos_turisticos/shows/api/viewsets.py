from rest_framework.viewsets import ModelViewSet
from shows.api.serializers import ShowSerializer
from shows.models import Show

class ShowViewSet(ModelViewSet):
    queryset         = Show.objects.all()
    serializer_class = ShowSerializer