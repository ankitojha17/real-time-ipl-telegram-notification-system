from django.http import JsonResponse


def home(request):
    return JsonResponse({
        "project": "Real-Time IPL Telegram Notification System",
        "status": "running",
        "version": "v1",
        "developer": "Ankit Ojha",
        "features": [
            "Live IPL Match Tracking",
            "Telegram Notifications",
            "Dockerized Deployment",
            "REST APIs",
            "JWT Authentication",
            "Cloud Hosted on Render"
        ],
        "api_endpoints": {
            "matches": "/api/v1/matches/live/",
            "notifications": "/api/v1/notifications/states/",
            "login": "/api/v1/users/login/",
            "preferences": "/api/v1/users/preferences/",
            "admin": "/admin/"
        }
    })