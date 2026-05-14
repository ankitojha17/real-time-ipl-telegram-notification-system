from django.urls import path
from apps.notifications.views import MatchStateView


urlpatterns=[
    path("states/",MatchStateView.as_view(),name="match-states"),
]