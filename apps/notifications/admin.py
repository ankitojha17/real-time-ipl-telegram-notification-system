from django.contrib import admin
from apps.notifications.models import MatchState,NotificationLog


@admin.register(MatchState)
class MatchStateAdmin(admin.ModelAdmin):
    list_display=["match","last_over","updated_at"]


@admin.register(NotificationLog)
class NotificationLogAdmin(admin.ModelAdmin):
    list_display=["user","match","event_type","status","created_at"]
    list_filter=["event_type","status"]
    search_fields=["user__phone_number"]