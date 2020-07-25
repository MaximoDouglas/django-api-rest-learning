from django.contrib import admin
from tourist_attractions.models import TouristAttraction
from tourist_attractions.models import IdentificationDocument

admin.site.register(TouristAttraction)
admin.site.register(IdentificationDocument)