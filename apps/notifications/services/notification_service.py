from apps.notifications.models import MatchState,NotificationLog
from apps.notifications.services.event_service import EventService
from apps.notifications.services.message_service import MessageService
from apps.notifications.services.whatsapp_api import WhatsAppApiService
from apps.users.selectors import UserPreferenceSelector


class NotificationService:

    @staticmethod
    def save_notification_log(user,match,event_type,message,status="sent"):
        NotificationLog.objects.create(user=user,match=match,event_type=event_type,message=message,status=status)

    @staticmethod
    def send_notification(users,match,event_type,message):
        for preference in users:
            sent=WhatsAppApiService.send_message(message)
            status="sent" if sent else "failed"
            NotificationService.save_notification_log(preference.user,match,event_type,message,status)

    @staticmethod
    def send_wicket_alert(match):
        users=UserPreferenceSelector.get_users_for_wicket_alert()
        NotificationService.send_notification(users,match,"wicket",MessageService.wicket_message(match))

    @staticmethod
    def send_six_alert(match):
        users=UserPreferenceSelector.get_users_for_six_alert()
        NotificationService.send_notification(users,match,"six",MessageService.six_message(match))

    @staticmethod
    def send_result_alert(match):
        users=UserPreferenceSelector.get_users_for_result_alert()
        NotificationService.send_notification(users,match,"result",MessageService.result_message(match))

    @staticmethod
    def send_over_update(match):
        users=UserPreferenceSelector.get_users_for_over_update()

        filtered=[]

        for preference in users:

            if preference.update_type=="5_over":
                try:
                    over=float(match.current_over)
                    whole=int(over)
                    ball=int(round((over-whole)*10))

                    if ball!=0 or whole%5!=0:
                        continue

                except Exception:
                    continue

            filtered.append(preference)

        NotificationService.send_notification(filtered,match,"over",MessageService.over_message(match))

    @staticmethod
    def update_match_state(match,data):

        state,created=MatchState.objects.get_or_create(match=match)

        old_score=state.last_team_one_score or "0/0"
        old_over=state.last_over or "0"

        new_score=data.get("team_one_score",old_score)
        new_team_two_score=data.get("team_two_score",state.last_team_two_score)
        new_over=data.get("current_over",old_over)

        match.team_one_score=new_score
        match.team_two_score=new_team_two_score
        match.current_over=new_over

        is_completed=EventService.detect_match_completed(match.status)

        if not is_completed:

            if EventService.detect_six(old_score,new_score):
                event=f"six_{new_score}"

                if state.last_six_event!=event:
                    NotificationService.send_six_alert(match)
                    state.last_six_event=event


            if EventService.detect_wicket(old_score,new_score):
                event=f"wicket_{new_score}"

                if state.last_wicket_event!=event:
                    NotificationService.send_wicket_alert(match)
                    state.last_wicket_event=event


            if EventService.detect_over_change(old_over,new_over):
                event=f"over_{new_over}"

                if state.last_over_event!=event:
                    NotificationService.send_over_update(match)
                    state.last_over_event=event


        if is_completed and state.last_result_event!="match_completed":
            NotificationService.send_result_alert(match)
            state.last_result_event="match_completed"


        state.last_team_one_score=new_score
        state.last_team_two_score=new_team_two_score
        state.last_over=new_over

        state.save()

        return state