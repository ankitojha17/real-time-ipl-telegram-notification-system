from django.db import models
from apps.matches.models import Match
from apps.users.models import User


class MatchState(models.Model):

    match=models.OneToOneField( Match, on_delete=models.CASCADE, related_name="match_state")
    last_team_one_score=models.CharField(max_length=50,blank=True,null=True )
    last_team_two_score=models.CharField( max_length=50, blank=True, null=True)
    last_over=models.CharField( max_length=20, blank=True, null=True)
    last_wicket_event=models.CharField( max_length=255, blank=True, null=True)
    last_six_event=models.CharField(max_length=255,blank=True,null=True)
    last_over_event=models.CharField(max_length=255,blank=True,null=True)
    last_result_event=models.CharField( max_length=255, blank=True, null=True)
    updated_at=models.DateTimeField(auto_now=True )

    def __str__(self):

        return str(self.match)
    

class NotificationLog(models.Model):
    EVENT_CHOICES=[("wicket","Wicket"),("six","Six"),("over","Over"),("result","Result")]
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    match=models.ForeignKey(Match,on_delete=models.CASCADE)
    event_type=models.CharField(max_length=20,choices=EVENT_CHOICES)
    message=models.TextField()
    status=models.CharField(max_length=20,default="sent")
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.phone_number} - {self.event_type}"