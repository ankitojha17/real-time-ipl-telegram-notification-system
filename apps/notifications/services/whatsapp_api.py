import logging
import requests

from django.conf import settings


logger=logging.getLogger(__name__)


class WhatsAppApiService:

    TIMEOUT=10

    @staticmethod
    def send_message(message):

        try:

            url=(
                f"https://api.telegram.org/"
                f"bot{settings.TELEGRAM_BOT_TOKEN}"
                f"/sendMessage"
            )

            payload={
                "chat_id":settings.TELEGRAM_CHAT_ID,
                "text":message
            }

            response=requests.post(
                url,
                data=payload,
                timeout=WhatsAppApiService.TIMEOUT
            )

            response.raise_for_status()

            data=response.json()

            if not data.get("ok"):

                logger.error(
                    f"Telegram error: {data}"
                )

                return False

            logger.info(
                "Message sent successfully"
            )

            return True


        except requests.exceptions.Timeout:

            logger.error(
                "Telegram timeout"
            )

        except requests.exceptions.RequestException as e:

            logger.error(
                f"Telegram request error: {str(e)}"
            )

        except Exception as e:

            logger.error(
                f"Unexpected error: {str(e)}"
            )

        return False