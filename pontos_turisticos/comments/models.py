from django.contrib.auth.models import User
from django.db import models
from tourist_attractions.models import TouristAttraction

class Comment(models.Model):
    user               = models.ForeignKey(User, on_delete=models.CASCADE)
    text               = models.TextField()
    date               = models.DateTimeField(auto_now_add=True)
    approved           = models.BooleanField(default=True)
    tourist_attraction = models.ForeignKey(TouristAttraction, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username
        