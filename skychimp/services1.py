from datetime import datetime
from smtplib import SMTPException
from django.utils.timezone import make_aware

from skychimp.models import MailingSetting, MailingLog
from django.core.mail import send_mail

from config import settings


def send_mailing():
    mailing_settings = MailingSetting.objects.all()  # Получаем все объекты рассылки
    current_datetime = datetime.now() #Получаем текущую дату и время
    current_datetime = make_aware(current_datetime)
    # Проверяем, должна ли рассылка быть запущена на данный момент
    for mailing_setting in mailing_settings:
        # Преобразование mailing_setting.time_start и mailing_setting.time_last_mailing в offset-aware даты/время
        mailing_setting.time_start = make_aware(mailing_setting.time_start)
        mailing_setting.time_last_mailing = make_aware(mailing_setting.time_last_mailing)
        # clients = mailing_setting.clients.all()
        # message = mailing_setting.message
        if mailing_setting.time_start <= current_datetime <= mailing_setting.time_last_mailing \
                and mailing_setting.status == 'N':
            mailing_setting.status = 'R'
    # mailing_settings.save()
    # if mailing_settings.status == 'R':
            clients = mailing_setting.clients.all()
            for client in clients:
                message = MailingSetting.message
                try:
                    send_mail(
                        subject=message.subject,
                        message=message.body,
                        from_email=settings.EMAIL_HOST_USER,
                        recipient_list=[client.email]
                    )
                    server_respond = 'success'
                    print(f'Рассылка успешно отправлена')
                    # Создание записи в логе рассылки
                    MailingLog.objects.create(
                        client=client,
                        mailing_setting=mailing_setting,
                        attempt_datetime=current_datetime,
                        server_response=server_respond,
                        status='C'
                        )
                except SMTPException as msg:
                    server_respond = f'error code: {msg}'
                    print(server_respond)
                    # Создание записи в логе рассылки
                    MailingLog.objects.create(
                        client=client,
                        mailing_setting=mailing_setting,
                        attempt_datetime=current_datetime,
                        server_response=server_respond,
                        status='R'
                    )
    mailing_settings.save()


# from django.utils import timezone
# from config import settings
#
#
# def str_to_time(str_to):
#     time = datetime.strptime(str_to, '%H:%M')
#     return time.time()
#
#
# class MailingManager:
#     def __init__(self, setting: MailingSetting):
#         self.setting = setting
#
#     def send_messages(self):
#         # Получение всех клиентов, связанных с данной настройкой рассылки
#         clients = self.setting.clients.all()
#         # Получение текущего времени
#         current_time = timezone.now().time()
#         send_time = self.setting.time_start
#         # Проверка текущего времени на соответствие временному интервалу рассылки
#         if str_to_time(send_time) <= current_time:    #<= self.end_time:
#             # Отправка сообщений для каждого клиента
#             for client in clients: