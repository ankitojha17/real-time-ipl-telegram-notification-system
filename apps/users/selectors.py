from apps.users.models import (
    User,
    UserPreference
)


class UserSelector:

    @staticmethod
    def get_user_by_phone(phone_number):

        return User.objects.filter(
            phone_number=phone_number
        ).first()

    @staticmethod
    def get_active_user_by_id(user_id):

        return User.objects.filter(
            id=user_id,
            is_active=True
        ).first()


class UserPreferenceSelector:

    @staticmethod
    def get_user_preferences(user):

        return UserPreference.objects.filter(
            user=user
        ).select_related("user").first()

    @staticmethod
    def get_users_for_wicket_alert():

        return UserPreference.objects.filter(
            wants_wicket_alert=True,
            user__is_active=True
        ).select_related("user")

    @staticmethod
    def get_users_for_result_alert():

        return UserPreference.objects.filter(
            wants_result_alert=True,
            user__is_active=True
        ).select_related("user")

    @staticmethod
    def get_users_for_over_update():

        return UserPreference.objects.filter(
            user__is_active=True
        ).select_related("user")
    
    @staticmethod
    def get_users_for_six_alert():

        return UserPreference.objects.filter(
            wants_six_alert=True,
            user__is_active=True
        ).select_related("user")