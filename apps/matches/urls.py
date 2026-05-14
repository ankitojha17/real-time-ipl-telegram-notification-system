from django.urls import path
from apps.matches.views import LiveMatchView


urlpatterns=[
    path("live/",LiveMatchView.as_view(),name="live-matches"),
]