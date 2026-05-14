from django.db import models

from utils.constants import (
    UPDATE_TYPE_5_OVER,
    UPDATE_TYPE_10_OVER,
    UPDATE_TYPE_KEY_MOMENT
)


class User(models.Model):

    phone_number=models.CharField(
        max_length=15,
        unique=True,
        db_index=True
    )

    is_active=models.BooleanField(default=True)

    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=["-created_at"]

    def __str__(self):
        return self.phone_number


class UserPreference(models.Model):

    UPDATE_CHOICES=[
        (UPDATE_TYPE_5_OVER,"5 Over"),
        (UPDATE_TYPE_10_OVER,"10 Over"),
        (UPDATE_TYPE_KEY_MOMENT,"Key Moment")
    ]

    user=models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="preferences"
    )

    update_type=models.CharField(
        max_length=20,
        choices=UPDATE_CHOICES,
        default=UPDATE_TYPE_KEY_MOMENT,
        db_index=True
    )

    wants_wicket_alert=models.BooleanField(default=True)
    wants_six_alert=models.BooleanField(default=True)
    wants_result_alert=models.BooleanField(default=True)
    wants_points_table=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=["-created_at"]

    def __str__(self):
        return f"{self.user.phone_number} Preferences"