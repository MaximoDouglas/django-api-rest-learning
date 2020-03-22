from django.db import models
from shows.models import Show
from enderecos.models import Endereco

class PontoTuristico(models.Model):
    nome      = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado  = models.BooleanField(default=False)
    shows     = models.ManyToManyField(Show)
    endereco  = models.ForeignKey(Endereco, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.nome