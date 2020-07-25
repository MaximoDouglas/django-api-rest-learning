from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from tourist_attractions.models import TouristAttraction
from tourist_attractions.models import IdentificationDocument
from shows.models import Show
from adresses.models import Address
from shows.api.serializers import ShowSerializer
from adresses.api.serializers import AddressSerializer

class IdentificationDocumentSerializer(ModelSerializer):
    class Meta:
        model  = IdentificationDocument
        fields = '__all__'

class TouristAttractionSerializer(ModelSerializer):
    shows                   = ShowSerializer(many=True)
    address                 = AddressSerializer()
    complete_description    = SerializerMethodField()
    identification_document = IdentificationDocumentSerializer()

    class Meta:
        model  = TouristAttraction
        fields = '__all__'
    
    def create_shows(self, shows, tourist_attraction):
        for show in shows:
             show_entry = Show.objects.create(**show)
             tourist_attraction.shows.add(show_entry)

        return tourist_attraction

    def create(self, validated_data):
        shows                   = validated_data['shows']
        address                 = validated_data['address']
        identification_document = validated_data['identification_document']
        
        del validated_data['shows'], validated_data['address'], validated_data['identification_document']

        tourist_attraction            = TouristAttraction.objects.create(**validated_data)
        address_entry                 = Address.objects.create(**address)
        identification_document_entry = IdentificationDocument.objects.create(**identification_document)
        
        self.create_shows(shows, tourist_attraction)
        tourist_attraction.address                 = address_entry
        tourist_attraction.identification_document = identification_document_entry

        tourist_attraction.save()
        return tourist_attraction

    def get_complete_description(self, object):
        return '%s - %s' % (object.name, object.description)