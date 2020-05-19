from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    name = "coronavirus"
    verbose_name = "Coronavirus"
