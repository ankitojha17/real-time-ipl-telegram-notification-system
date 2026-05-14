from rest_framework import serializers
from apps.notifications.models import MatchState


class MatchStateSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    last_team_one_score=serializers.CharField()
    last_team_two_score=serializers.CharField()
    last_over=serializers.CharField()
    last_event=serializers.CharField()
    updated_at=serializers.DateTimeField(read_only=True)

    def to_representation(self,instance):

        return {
            "id":instance.id,
            "last_team_one_score":instance.last_team_one_score,
            "last_team_two_score":instance.last_team_two_score,
            "last_over":instance.last_over,
            "last_event":instance.last_event,
            "updated_at":instance.updated_at
        }