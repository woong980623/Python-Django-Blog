from django.apps import AppConfig

class Blog1Config(AppConfig):
    name = 'blog1'

    def ready(self):
        import blog1.signals
