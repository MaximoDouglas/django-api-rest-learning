from rest_framework.serializers import ModelSerializer
from tourist_attractions.models import TouristAttraction
from shows.api.serializers import ShowSerializer
from adresses.api.serializers import AddressSerializer

class TouristAttractionSerializer(ModelSerializer):
    shows   = ShowSerializer(many=True)
    address = AddressSerializer()
    
    class Meta:
        model  = TouristAttraction
        fields = '__all__'