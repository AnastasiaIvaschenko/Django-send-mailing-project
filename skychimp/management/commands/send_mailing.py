from django.core.management import BaseCommand
from skychimp.services2 import send_mailing


class Command(BaseCommand):
    def handle(self, *args, **options):
        send_mailing()

