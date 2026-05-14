from django.apps import AppConfig


class NotificationsConfig(AppConfig):
    default_auto_field="django.db.models.BigAutoField"
    name="apps.notifications"

    def ready(self):
        import os

        if os.environ.get("RUN_MAIN")=="true":
            from apps.notifications.scheduler import start_scheduler
            start_scheduler()