from django.db import models

from utils.constants import (MATCH_STATUS_LIVE,MATCH_STATUS_COMPLETED)


class Team(models.Model):
    name=models.CharField(max_length=100)
    short_name=models.CharField(max_length=10)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Match(models.Model):

    MATCH_STATUS_CHOICES=[
        (MATCH_STATUS_LIVE,"Live"),
        (MATCH_STATUS_COMPLETED,"Completed")
    ]

    team_one=models.ForeignKey(Team,on_delete=models.CASCADE,related_name="team_one_matches")
    team_two=models.ForeignKey(Team,on_delete=models.CASCADE,related_name="team_two_matches")
    team_one_score=models.CharField(max_length=50,blank=True,null=True)
    team_two_score=models.CharField(max_length=50,blank=True,null=True)
    current_over=models.CharField(max_length=20,blank=True,null=True)
    status=models.CharField(max_length=20,choices=MATCH_STATUS_CHOICES,default=MATCH_STATUS_LIVE)
    match_time=models.DateTimeField()
    venue=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.team_one.short_name} vs {self.team_two.short_name}"