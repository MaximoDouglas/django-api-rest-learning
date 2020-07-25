from rest_framework.serializers import ModelSerializer
from shows.models import Show

class ShowSerializer(ModelSerializer):
    class Meta:
        model = Show
        fields = '__all__'