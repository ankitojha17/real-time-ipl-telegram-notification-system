from rest_framework_simplejwt.tokens import AccessToken

from apps.users.models import User


def get_authenticated_user(request):

    auth_header=request.headers.get("Authorization")

    if not auth_header:
        return None

    token=auth_header.split(" ")[1]

    decoded_token=AccessToken(token)

    user_id=decoded_token.get("user_id")

    return User.objects.filter(id=user_id).first()