from django.contrib.auth.models import User
from django.db import models
from core.models import PontoTuristico

class Comment(models.Model):
    user             = models.ForeignKey(User, on_delete=models.CASCADE)
    text             = models.TextField()
    date             = models.DateTimeField(auto_now_add=True)
    approved         = models.BooleanField(default=True)
    attraction_place = models.ForeignKey(PontoTuristico, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username
        