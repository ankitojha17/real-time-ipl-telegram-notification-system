import logging

from apscheduler.schedulers.background import BackgroundScheduler
from apps.notifications.services.cricket_api import CricketApiService
from apps.notifications.tasks import process_live_matches

logger=logging.getLogger(__name__)

scheduler=None

def run_notification_engine():
    try:
        logger.info("Syncing live matches...")

        CricketApiService.sync_live_matches()

        logger.info("Processing notifications...")

        process_live_matches()

        logger.info("Notification cycle completed")

    except Exception as e:
        logger.error(f"Notification Engine Error: {str(e)}")

def start_scheduler():
    global scheduler

    if scheduler and scheduler.running:
        return

    scheduler=BackgroundScheduler()

    scheduler.add_job(
        run_notification_engine,
        "interval",
        seconds=15,
        id="ipl_notification_engine",
        max_instances=1,
        coalesce=True,
        replace_existing=True
    )

    scheduler.start()

    logger.info("Scheduler started successfully")