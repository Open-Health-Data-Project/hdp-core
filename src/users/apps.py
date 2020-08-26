from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):    # from signals.py
        import users.signals
