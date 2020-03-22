from django.db import models
from shows.models import Show
from adresses.models import Address

class TouristAttraction(models.Model):
    name        = models.CharField(max_length=150)
    description = models.TextField()
    approved    = models.BooleanField(default=False)
    shows       = models.ManyToManyField(Show)
    address     = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.name