class MessageService:

    @staticmethod
    def format_score(score):

        if not score:
            return "Yet to bat"

        if score=="0/0":
            return "Yet to bat"

        return score

    @staticmethod
    def format_match_title(match):

        return (
            f"{match.team_one.short_name} vs "
            f"{match.team_two.short_name}"
        )

    @staticmethod
    def format_over(over):

        try:

            over_float=float(over)

            whole=int(over_float)

            decimal=int(
                round(
                    (over_float-whole)*10
                )
            )


            if decimal>=6:

                whole+=1

                decimal=0

            return f"{whole}.{decimal}"

        except:

            return over

    @staticmethod
    def wicket_message(match):

        return (
            f"🏏 WICKET ALERT\n\n"
            f"{MessageService.format_match_title(match)}\n\n"
            f"{match.team_one.short_name}: "
            f"{MessageService.format_score(match.team_one_score)}\n"
            f"{match.team_two.short_name}: "
            f"{MessageService.format_score(match.team_two_score)}\n\n"
            f"Over: "
            f"{MessageService.format_over(match.current_over)}\n\n"
            f"🔥 Big breakthrough!"
        )

    @staticmethod
    def six_message(match):

        return (
            f"💥 SIX ALERT\n\n"
            f"{MessageService.format_match_title(match)}\n\n"
            f"{match.team_one.short_name}: "
            f"{MessageService.format_score(match.team_one_score)}\n"
            f"{match.team_two.short_name}: "
            f"{MessageService.format_score(match.team_two_score)}\n\n"
            f"Over: "
            f"{MessageService.format_over(match.current_over)}\n\n"
            f"🚀 Massive six!"
        )

    @staticmethod
    def over_message(match):

        return (
            f"📢 OVER UPDATE\n\n"
            f"{MessageService.format_match_title(match)}\n\n"
            f"{match.team_one.short_name}: "
            f"{MessageService.format_score(match.team_one_score)}\n"
            f"{match.team_two.short_name}: "
            f"{MessageService.format_score(match.team_two_score)}\n\n"
            f"📍 "
            f"{int(float(match.current_over))} "
            f"Overs Completed"
        )

    @staticmethod
    def result_message(match):

        return (
            f"🏆 MATCH RESULT\n\n"
            f"{MessageService.format_match_title(match)}\n\n"
            f"{match.team_one.short_name}: "
            f"{MessageService.format_score(match.team_one_score)}\n"
            f"{match.team_two.short_name}: "
            f"{MessageService.format_score(match.team_two_score)}\n\n"

            f"✅ Match Completed"
        )