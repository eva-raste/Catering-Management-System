from django.apps import AppConfig
from django.db import OperationalError


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'

    def ready(self):
        from .models import Cuisine  # Import your model here
        CUISINE_TYPE_CHOICES = [
            ('PUNJABI', 'PUNJABI'),
            ('SOUTH INDIAN', 'SOUTH INDIAN'),
            ('GUJARATI', 'GUJARATI'),
            ('RAJASTHANI', 'RAJASTHANI'),
            ('MAHARASHTRIAN', 'MAHARASHTRIAN'),
            ('ITALIAN', 'ITALIAN'),
            ('CHINESE', 'CHINESE'),
            ('MEXICAN', 'MEXICAN'),
            ('THAI', 'THAI'),
            ('JAPANESE', 'JAPANESE')
        ]

        try:
            for cuisine in CUISINE_TYPE_CHOICES:
                Cuisine.objects.get_or_create(name=cuisine[0])
        except OperationalError:
            # This prevents issues when running `migrate` before the database exists
            pass