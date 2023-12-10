from django.core.management import BaseCommand

from skychimp.services1 import send_mailing


class Command(BaseCommand):

    def handle(self, *args, **options):
        send_mailing()

# from apscheduler.schedulers.background import BackgroundScheduler
#
# # Создаем экземпляр планировщика задач
# scheduler = BackgroundScheduler()
#
# # Определяем функцию, которая будет вызываться планировщиком для выполнения отправки рассылок
# def send_mailings_job():
#     mailing_manager.send_mailings()
#
# # Запускаем задачу отправки рассылок по расписанию
# scheduler.add_job(send_mailings_job, 'interval', hours=1)  # Например, отправка каждый час
#
# # Запускаем планировщик
# scheduler.start()

        # send_mail(
        #         subject='Вы сменили пароль',
        #         message=f'Ваш новый пароль 12345',
        #         from_email=EMAIL_HOST_USER,
        #         recipient_list=['anivasch@mail.ru'],
        #         fail_silently=False,
        # )

