import os
import logging
import requests

from apps.matches.services import MatchService


logger=logging.getLogger(__name__)


class CricketApiService:

    BASE_URL="https://cricbuzz-cricket.p.rapidapi.com"

    HEADERS={
        "X-RapidAPI-Key":os.getenv("RAPID_API_KEY",""),
        "X-RapidAPI-Host":"cricbuzz-cricket.p.rapidapi.com"
    }

    @staticmethod
    def get_live_matches():

        try:

            response=requests.get(
                f"{CricketApiService.BASE_URL}/matches/v1/live",
                headers=CricketApiService.HEADERS,
                timeout=10
            )

            response.raise_for_status()

            return response.json()

        except requests.exceptions.Timeout:

            logger.error(
                "Cricket API timeout"
            )

        except requests.exceptions.RequestException as e:

            logger.error(
                f"Cricket API error: {str(e)}"
            )

        except Exception as e:

            logger.error(
                f"Unexpected error: {str(e)}"
            )

        return {}


    @staticmethod
    def sync_live_matches():

        data=CricketApiService.get_live_matches()

        if not data:

            logger.warning(
                "No match data received"
            )

            return False


        type_matches=data.get(
            "typeMatches",
            []
        )

        for type_match in type_matches:

            series_matches=type_match.get(
                "seriesMatches",
                []
            )

            for series in series_matches:

                wrapper=series.get(
                    "seriesAdWrapper",
                    {}
                )

                matches=wrapper.get(
                    "matches",
                    []
                )

                for match in matches:

                    try:

                        MatchService.create_or_update_match(
                            match
                        )

                    except Exception as e:

                        logger.error(
                            f"Match sync error: {str(e)}"
                        )

        logger.info(
            "Live matches synced successfully"
        )

        return True