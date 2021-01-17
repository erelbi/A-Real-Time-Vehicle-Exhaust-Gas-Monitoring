from django.apps import AppConfig


class SensorsConfig(AppConfig):
    name = 'sensors'

    def ready(self):
        from . import signals