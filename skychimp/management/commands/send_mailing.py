from django.core.mail import send_mail
from django.core.management.base import BaseCommand

from config.settings import EMAIL_HOST_USER
# from skychimp.services import MailingManager


class Command(BaseCommand):
    help = 'Send mailing messages'

    def handle(self, *args, **options):
        # mailing_manager = MailingManager()
        # mailing_manager.send_messages()
        send_mail(
            subject='test',
            message='test',
            from_email=EMAIL_HOST_USER,
            recipient_list=['ivashch84@yandex.ru']

        )
