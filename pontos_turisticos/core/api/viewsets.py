from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from core.api.serializers import PontoTuristicoSerializer
from rest_framework.response import Response
from rest_framework.decorators import action

class PontoTuristicoViewSet(ModelViewSet):
    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)

    @action(methods=['get'], detail=True)
    def showname(self, request, pk=None):
        pontoTuristico = self.get_object()
        return Response({"Name": pontoTuristico.nome})