from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from apps.users.serializers import (LoginSerializer,UserSerializer,UserPreferenceSerializer)
from apps.users.services import (UserService,UserPreferenceService)
from apps.users.selectors import (UserPreferenceSelector)
from apps.users.tokens import generate_tokens
from utils.authentication import get_authenticated_user
from utils.response_wrapper import ApiResponse


class LoginView(APIView):

    permission_classes=[AllowAny]

    def post(self,request):

        serializer=LoginSerializer(data=request.data)

        if not serializer.is_valid():
            return ApiResponse.error(
                message="Validation failed.",
                errors=serializer.errors
            )

        phone_number=serializer.validated_data["phone_number"]

        user=UserService.get_or_create_user(
            phone_number
        )

        tokens=generate_tokens(user)

        return ApiResponse.success(
            message="Login successful.",
            data={
                "user":UserSerializer(user).data,
                "tokens":tokens
            }
        )


class UserPreferenceView(APIView):

    def get(self,request):

        user=get_authenticated_user(request)

        if not user:
            return ApiResponse.error(
                message="Authentication failed.",
                status_code=401
            )

        preferences=UserPreferenceSelector.get_user_preferences(
            user
        )

        return ApiResponse.success(
            message="Preferences fetched successfully.",
            data=UserPreferenceSerializer(preferences).data if preferences else {}
        )

    def put(self,request):

        user=get_authenticated_user(request)

        if not user:
            return ApiResponse.error(
                message="Authentication failed.",
                status_code=401
            )

        serializer=UserPreferenceSerializer(
            data=request.data
        )

        if not serializer.is_valid():
            return ApiResponse.error(
                message="Validation failed.",
                errors=serializer.errors
            )

        preferences=UserPreferenceService.update_preferences(
            user,
            serializer.validated_data
        )

        return ApiResponse.success(
            message="Preferences updated successfully.",
            data=UserPreferenceSerializer(preferences).data
        )