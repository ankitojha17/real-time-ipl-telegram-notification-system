from django.core.management.base import BaseCommand

from apps.notifications.services.cricket_api import CricketApiService

from apps.notifications.tasks import process_live_matches


class Command(BaseCommand):

    help="Process live IPL matches"

    def handle(self,*args,**kwargs):

        CricketApiService.sync_live_matches()

        process_live_matches()

        self.stdout.write(
            self.style.SUCCESS(
                "Live matches synced successfully."
            )
        )