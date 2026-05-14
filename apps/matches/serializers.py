from rest_framework import serializers

from apps.matches.models import (Team,Match)


class TeamSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField()
    short_name=serializers.CharField()

    def to_representation(self,instance):
        return {
            "id":instance.id,
            "name":instance.name,
            "short_name":instance.short_name
        }


class MatchSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    team_one=TeamSerializer(read_only=True)
    team_two=TeamSerializer(read_only=True)
    team_one_score=serializers.CharField()
    team_two_score=serializers.CharField()
    current_over=serializers.CharField()
    status=serializers.CharField()
    match_time=serializers.DateTimeField()
    venue=serializers.CharField()

    def to_representation(self,instance):
        return {
            "id":instance.id,
            "team_one":TeamSerializer(instance.team_one).data,
            "team_two":TeamSerializer(instance.team_two).data,
            "team_one_score":instance.team_one_score,
            "team_two_score":instance.team_two_score,
            "current_over":instance.current_over,
            "status":instance.status,
            "match_time":instance.match_time,
            "venue":instance.venue
        }