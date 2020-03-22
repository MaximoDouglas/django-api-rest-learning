from django.db import models
from django.contrib.auth.models import User
from tourist_attractions.models import TouristAttraction

class Rating(models.Model):
    user               = models.ForeignKey(User, on_delete=models.CASCADE)
    tourist_attraction = models.ForeignKey(TouristAttraction, on_delete=models.CASCADE)
    comments           = models.TextField(null=True, blank=True)
    rating             = models.DecimalField(max_digits=3, decimal_places=2)
    date               = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username