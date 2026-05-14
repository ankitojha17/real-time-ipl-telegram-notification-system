import logging

logger=logging.getLogger(__name__)

class EventService:

    @staticmethod
    def extract_runs(score):
        try:
            if not score:
                return 0
            return int(str(score).split("/")[0])
        except Exception as e:
            logger.warning(f"Run extraction error: {str(e)}")
            return 0

    @staticmethod
    def extract_wickets(score):
        try:
            if not score:
                return 0
            parts=str(score).split("/")
            if len(parts)<2:
                return 0
            return int(parts[1])
        except Exception as e:
            logger.warning(f"Wicket extraction error: {str(e)}")
            return 0

    @staticmethod
    def extract_over(over):
        try:
            return float(over)
        except Exception as e:
            logger.warning(f"Over extraction error: {str(e)}")
            return 0

    @staticmethod
    def detect_wicket(old_score,new_score):
        old_wicket=EventService.extract_wickets(old_score)
        new_wicket=EventService.extract_wickets(new_score)
        return new_wicket>old_wicket

    @staticmethod
    def detect_six(old_score,new_score):
        old_runs=EventService.extract_runs(old_score)
        new_runs=EventService.extract_runs(new_score)
        return (new_runs-old_runs)==6

    @staticmethod
    def detect_over_change(old_over,new_over):
        old_over=EventService.extract_over(old_over)
        new_over=EventService.extract_over(new_over)
        return new_over>old_over

    @staticmethod
    def detect_match_completed(status):
        return str(status).upper()=="COMPLETED"