import logging

from apps.matches.selectors import MatchSelector
from apps.notifications.services.notification_service import NotificationService

logger=logging.getLogger(__name__)

def process_live_matches():
    try:
        matches=MatchSelector.get_live_matches()

        if not matches:
            logger.warning("No live matches found")
            return False

        for match in matches:
            try:
                NotificationService.update_match_state(
                    match,
                    {
                        "team_one_score":match.team_one_score,
                        "team_two_score":match.team_two_score,
                        "current_over":match.current_over
                    }
                )
            except Exception as e:
                logger.error(f"Match processing error: {str(e)}")

        logger.info(f"{len(matches)} live matches processed")
        return True

    except Exception as e:
        logger.error(f"Live match task failed: {str(e)}")
        return False