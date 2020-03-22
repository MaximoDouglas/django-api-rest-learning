from rest_framework.viewsets import ModelViewSet
from tourist_attractions.models import TouristAttraction
from tourist_attractions.api.serializers import TouristAttractionSerializer
from rest_framework.response import Response
from rest_framework.decorators import action

class TouristAttractionViewSet(ModelViewSet):
    serializer_class = TouristAttractionSerializer

    def get_queryset(self):
        return TouristAttraction.objects.filter(approved=True)

    @action(methods=['get'], detail=True)
    def showname(self, request, pk=None):
        touristAttraction = self.get_object()
        return Response({"Name": touristAttraction.name})