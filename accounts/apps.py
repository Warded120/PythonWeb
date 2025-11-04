from django.apps import AppConfig
from django.core.exceptions import ImproperlyConfigured
from django.core.management import call_command
from django.db import OperationalError


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        try:
            call_command('migrate', '--noinput')
            call_command('loaddata', 'accounts')
            print("✅ Account fixtures loaded.")
        except (OperationalError, ImproperlyConfigured):
            pass