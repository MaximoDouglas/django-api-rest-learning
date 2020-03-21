from django.db import models

class Endereco(models.Model):
    logradouro  = models.CharField(max_length=150)
    bairro      = models.CharField(max_length=150, null=True, blank=True)
    complemento = models.CharField(max_length=150)
    cidade      = models.CharField(max_length=100)
    estado      = models.CharField(max_length=50)
    pais        = models.CharField(max_length=70)
    latitude    = models.IntegerField(null=True, blank=True)
    longitude   = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.logradouro