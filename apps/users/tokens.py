from rest_framework_simplejwt.tokens import RefreshToken


def generate_tokens(user):

    refresh=RefreshToken()

    refresh["user_id"]=user.id
    refresh["phone_number"]=user.phone_number

    return {
        "refresh":str(refresh),
        "access":str(refresh.access_token)
    }