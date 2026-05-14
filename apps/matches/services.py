from datetime import datetime

from django.utils.timezone import make_aware

from apps.matches.models import Team
from apps.matches.models import Match

from utils.constants import MATCH_STATUS_LIVE
from utils.constants import MATCH_STATUS_COMPLETED


class MatchService:

    @staticmethod
    def get_or_create_team(team_data):

        team,_=Team.objects.get_or_create(
            name=team_data["teamName"],
            defaults={
                "short_name":team_data["teamSName"]
            }
        )

        return team

    @staticmethod
    def create_or_update_match(match_data):

        match_info=match_data.get("matchInfo",{})

        match_score=match_data.get("matchScore",{})

        team_one=MatchService.get_or_create_team(
            match_info["team1"]
        )

        team_two=MatchService.get_or_create_team(
            match_info["team2"]
        )

        team_one_score=match_score.get("team1Score",{})

        team_two_score=match_score.get("team2Score",{})

        innings_one=team_one_score.get("inngs1",{})

        innings_two=team_two_score.get("inngs1",{})

        match_status=MATCH_STATUS_LIVE

        if match_info.get("state")=="Complete":
            match_status=MATCH_STATUS_COMPLETED

        match,_=Match.objects.update_or_create(

            id=match_info["matchId"],

            defaults={

                "team_one":team_one,

                "team_two":team_two,

                "team_one_score":
                    f'{innings_one.get("runs",0)}/{innings_one.get("wickets",0)}',

                "team_two_score":
                    f'{innings_two.get("runs",0)}/{innings_two.get("wickets",0)}',

                "current_over":
                    str(innings_one.get("overs","0")),

                "status":match_status,

                "venue":
                    match_info.get("venueInfo",{}).get("ground",""),

                "match_time":
                    make_aware(
                        datetime.fromtimestamp(
                            int(match_info.get("startDate"))/1000
                        )
                    )
            }
        )

        return match