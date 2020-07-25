from rest_framework.viewsets import ModelViewSet
from adresses.models import Address
from adresses.api.serializers import AddressSerializer

class AdressViewSet(ModelViewSet):
    queryset         = Address.objects.all()
    serializer_class = AddressSerializer