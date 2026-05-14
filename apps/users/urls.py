from django.urls import path

from apps.users.views import (
    LoginView,
    UserPreferenceView
)


urlpatterns=[
    path("login/",LoginView.as_view(),name="login"),
    path("preferences/",UserPreferenceView.as_view(),name="preferences"),
]