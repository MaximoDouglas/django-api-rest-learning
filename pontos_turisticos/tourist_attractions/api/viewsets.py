from rest_framework.viewsets import ModelViewSet
from django.db.models import Q
from django.http import HttpResponse
from tourist_attractions.models import TouristAttraction
from shows.models import Show
from tourist_attractions.api.serializers import TouristAttractionSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.decorators import action

class TouristAttractionViewSet(ModelViewSet):
    serializer_class       = TouristAttractionSerializer
    filter_backends        = (SearchFilter,)
    search_fields          = ('name', 'description', 'address__street')
    lookup_field           = 'guid'
    permission_classes     = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

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

    @action(methods=['post'], detail=True)
    def shows_association(self, request, guid=None):
        show_ids           = request.data['id_list']
        tourist_attraction = TouristAttraction.objects.get(guid=guid)
        
        tourist_attraction.shows.set(show_ids)
        tourist_attraction.save()

        show_names = []
        for id in show_ids:
            show_entry = Show.objects.get(id=id)
            show_names.append(show_entry.name) 
        
        return Response({"shows": show_names, 
                        "attraction_point_name": tourist_attraction.name, 
                        "attraction_point_id": tourist_attraction.id})