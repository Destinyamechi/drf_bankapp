from django.apps import AppConfig


class AccountappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Accountapp'

    def ready(self):
        import Accountapp.signals
