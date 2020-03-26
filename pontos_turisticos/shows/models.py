from django.db import models

class Show(models.Model):
    name          = models.CharField(max_length=150)
    description   = models.TextField()
    working_shift = models.TextField()
    min_age       = models.IntegerField()
    photo         = models.ImageField(upload_to='shows', null=True, blank=True)
    notes         = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.name