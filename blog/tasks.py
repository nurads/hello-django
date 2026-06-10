import logging

from celery import shared_task

logger = logging.getLogger(__name__)


@shared_task
def heartbeat():
    logger.info("Celery Beat heartbeat task ran")
    return "ok"
