from rest_framework.throttling import UserRateThrottle


class UserThrottle(UserRateThrottle):
    rate = "100/min"