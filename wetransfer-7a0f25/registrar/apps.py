from django.apps import AppConfig


class RegistrarConfig(AppConfig):
    name = 'registrar'

    def ready(self):
        # import signal handlers
        import registrar.signals