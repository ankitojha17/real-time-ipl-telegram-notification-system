from rest_framework import serializers

from apps.users.models import (
    User,
    UserPreference
)


class UserSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    phone_number=serializers.CharField(max_length=15)
    is_active=serializers.BooleanField(read_only=True)
    created_at=serializers.DateTimeField(read_only=True)

    def to_representation(self,instance):
        return {
            "id":instance.id,
            "phone_number":instance.phone_number,
            "is_active":instance.is_active,
            "created_at":instance.created_at
        }


class LoginSerializer(serializers.Serializer):
    phone_number=serializers.CharField(max_length=15)


class UserPreferenceSerializer(serializers.Serializer):
    update_type=serializers.CharField()
    wants_wicket_alert=serializers.BooleanField()
    wants_six_alert=serializers.BooleanField()
    wants_result_alert=serializers.BooleanField()
    wants_points_table=serializers.BooleanField()

    def to_representation(self,instance):
        return {
            "update_type":instance.update_type,
            "wants_wicket_alert":instance.wants_wicket_alert,
            "wants_six_alert":instance.wants_six_alert,
            "wants_result_alert":instance.wants_result_alert,
            "wants_points_table":instance.wants_points_table
        }