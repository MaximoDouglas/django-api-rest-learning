import random
import string
from django.db import models
from shows.models import Show
from adresses.models import Address

def randomString():
    stringLength = 10
    letters      = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

class IdentificationDocument(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description

class TouristAttraction(models.Model):
    guid                    = models.CharField(editable=False, default=randomString, max_length=10)
    name                    = models.CharField(max_length=150)
    description             = models.TextField()
    approved                = models.BooleanField(default=False)
    shows                   = models.ManyToManyField(Show)
    address                 = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True)
    photo                   = models.ImageField(upload_to='tourist_attractions', null=True, blank=True)
    identification_document = models.OneToOneField(IdentificationDocument, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.name