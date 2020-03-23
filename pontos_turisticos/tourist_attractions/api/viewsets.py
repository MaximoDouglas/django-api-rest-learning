from rest_framework.viewsets import ModelViewSet
from django.db.models import Q
from tourist_attractions.models import TouristAttraction
from tourist_attractions.api.serializers import TouristAttractionSerializer
from rest_framework.response import Response
from rest_framework.decorators import action

class TouristAttractionViewSet(ModelViewSet):
    serializer_class = TouristAttractionSerializer

    def get_queryset(self):
        id          = self.request.query_params.get('id', None)
        name        = self.request.query_params.get('name', None)
        description = self.request.query_params.get('description', None)

        queryset = TouristAttraction.objects.all()

        if (id and name):
            id_query                    = Q(pk=id)
            name_query_case_insensitive = Q(name__iexact=name)

            queryset = queryset.filter(id_query | name_query_case_insensitive)

        if description:
            queryset = queryset.filter(description=description)

        return queryset

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