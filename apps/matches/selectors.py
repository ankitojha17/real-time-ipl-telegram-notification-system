from apps.matches.models import Match


class MatchSelector:

    @staticmethod
    def get_live_matches():

        return Match.objects.filter(status="LIVE").select_related("team_one","team_two")

    @staticmethod
    def get_today_matches():

        return Match.objects.select_related("team_one","team_two").all()