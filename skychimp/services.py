# from datetime import datetime
# from smtplib import SMTPException
#
# from django.core.mail import send_mail
#
# from skychimp.models import Client, MailingSetting, Message, MailingLog, Subscription
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
#     def send_messages(self):
#         # Получение всех клиентов, связанных с данной настройкой рассылки
#         clients = self.setting.clients
#         # Получение текущего времени
#         current_time = timezone.now().time()
#         send_time = self.setting.time_start
#         # Проверка текущего времени на соответствие временному интервалу рассылки
#         if str_to_time(send_time) <= current_time:    #<= self.end_time:
#             # Отправка сообщений для каждого клиента
#             for client_id in clients.objects.all():
#                 client = Client.objects.get(id=client_id)
#                 message = Message.objects.get(mailing_setting=self.setting)
#                 # Отправка сообщения и обработка ошибок
#                 try:
#                     send_mail(
#                         subject=message.subject,
#                         message=message.body,
#                         from_email=settings.EMAIL_HOST_USER,
#                         recipient_list=client
#                     )
#                     server_respond = 'success'
#                     print(f'Рассылка "{self.setting}" успешно отправлена')
#                     # Создание записи в логе рассылки
#                     MailingLog.objects.create(
#                         client=client,
#                         mailing_setting=self.setting,
#                         attempt_datetime=current_time,
#                         server_response=server_respond,
#                         status='C'
#                     )
#                 except SMTPException as msg:
#                     server_respond = f'error code: {msg}'
#                     print(server_respond)
#                     # Создание записи в логе рассылки
#                     MailingLog.objects.create(
#                         client=client,
#                         mailing_setting=self.setting,
#                         attempt_datetime=current_time,
#                         server_response=server_respond,
#                         status='R'
#                     )
#
#
#     def create_subscription(self, client, mailing_setting, subscribed_date):
#         # Создание подписки для клиента на определенную рассылку
#         Subscription.objects.create(client=client, mailing_setting=mailing_setting, subscribed_date=subscribed_date)
#
#
#     def start_scheduled_delivery(self):
#         # Получение всех настроек рассылок со временем старта в будущем
#         scheduled_mailings = MailingSetting.objects.filter(start_time__gt=timezone.now())
#
#         # Запуск автоматической отправки при достижении времени старта
#         for mailing in scheduled_mailings:
#             mailing.send_messages()
