from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from tourist_attractions.models import TouristAttraction
from shows.api.serializers import ShowSerializer
from adresses.api.serializers import AddressSerializer

class TouristAttractionSerializer(ModelSerializer):
    shows                = ShowSerializer(many=True)
    address              = AddressSerializer()
    complete_description = SerializerMethodField()

    class Meta:
        model  = TouristAttraction
        fields = '__all__'

    def get_complete_description(self, object):
        return '%s - %s' % (object.name, object.description)