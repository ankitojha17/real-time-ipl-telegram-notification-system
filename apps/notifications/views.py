from rest_framework.views import APIView
from apps.notifications.models import MatchState
from apps.notifications.serializers import MatchStateSerializer
from utils.response_wrapper import ApiResponse


class MatchStateView(APIView):

    def get(self,request):

        states=MatchState.objects.select_related("match").all()
        serializer=MatchStateSerializer(states,many=True)

        return ApiResponse.success(
            message="Match states fetched successfully.",
            data=serializer.data
        )