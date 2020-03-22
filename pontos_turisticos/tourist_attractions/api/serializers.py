from rest_framework.serializers import ModelSerializer
from tourist_attractions.models import TouristAttraction

class TouristAttractionSerializer(ModelSerializer):
    class Meta:
        model  = TouristAttraction
        fields = '__all__'