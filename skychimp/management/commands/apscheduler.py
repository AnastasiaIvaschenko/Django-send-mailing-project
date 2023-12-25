from django.core.management.base import BaseCommand
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.interval import IntervalTrigger  # Импорт IntervalTrigger
from skychimp.services2 import send_mailing

scheduler = BlockingScheduler()


class Command(BaseCommand):
    def handle(self, *args, **options):
        scheduler.add_job(send_mailing, trigger=IntervalTrigger(seconds=10))  # Здесь можно настроить интервал отправки сообщений

        try:
            scheduler.start()
        except (KeyboardInterrupt, SystemExit):
            scheduler.shutdown()
