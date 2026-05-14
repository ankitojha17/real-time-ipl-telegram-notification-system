from rest_framework.views import APIView
from apps.matches.selectors import MatchSelector
from apps.matches.serializers import MatchSerializer
from utils.response_wrapper import ApiResponse
from utils.authentication import get_authenticated_user


class LiveMatchView(APIView):

    def get(self,request):

        user=get_authenticated_user(request)

        if not user:
            return ApiResponse.error(
                message="Authentication failed.",
                status_code=401
            )

        matches=MatchSelector.get_live_matches()

        serializer=MatchSerializer(
            matches,
            many=True
        )

        return ApiResponse.success(
            message="Live matches fetched successfully.",
            data=serializer.data
        )