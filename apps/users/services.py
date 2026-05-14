from apps.users.models import (
    User,
    UserPreference
)


class UserService:

    @staticmethod
    def get_or_create_user(phone_number):

        user,created=User.objects.get_or_create(
            phone_number=phone_number
        )

        return user


class UserPreferenceService:

    @staticmethod
    def update_preferences(user,validated_data):

        preference,created=UserPreference.objects.get_or_create(
            user=user
        )

        preference.update_type=validated_data.get(
            "update_type",
            preference.update_type
        )

        preference.wants_wicket_alert=validated_data.get(
            "wants_wicket_alert",
            preference.wants_wicket_alert
        )

        preference.wants_six_alert=validated_data.get(
            "wants_six_alert",
            preference.wants_six_alert
        )

        preference.wants_result_alert=validated_data.get(
            "wants_result_alert",
            preference.wants_result_alert
        )

        preference.wants_points_table=validated_data.get(
            "wants_points_table",
            preference.wants_points_table
        )

        preference.save()

        return preference