from rest_framework.viewsets import ModelViewSet
from tourist_attractions.models import TouristAttraction
from tourist_attractions.api.serializers import TouristAttractionSerializer
from rest_framework.response import Response
from rest_framework.decorators import action

class TouristAttractionViewSet(ModelViewSet):
    serializer_class = TouristAttractionSerializer

    def get_queryset(self):
        return TouristAttraction.objects.filter(approved=True)

    def list(self, request, *args, **kwargs):
        return super(TouristAttractionViewSet, self).list(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        return super(TouristAttractionViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(TouristAttractionViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(TouristAttractionViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(TouristAttractionViewSet, self).update(request, *args, **kwargs)

    @action(methods=['get'], detail=True)
    def showname(self, request, pk=None):
        touristAttraction = self.get_object()
        return Response({"Name": touristAttraction.name})