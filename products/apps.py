from django.apps import AppConfig
from django.core.exceptions import ImproperlyConfigured
from django.core.management import call_command
from django.db import OperationalError


class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'

    def ready(self):
        from .models import Product
        try:
            call_command('migrate', '--noinput')
            call_command('loaddata', 'products')
            print("✅ Product fixtures loaded.")
        except (OperationalError, ImproperlyConfigured):
            pass