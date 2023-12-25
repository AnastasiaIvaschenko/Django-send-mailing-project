# # from smtplib import SMTPException
# from django.utils.timezone import now
#
# from skychimp.models import MailingSetting, MailingLog
# from django.core.mail import send_mail
# from config import settings
#
#
# def send_message(setting):
#     mailing_clients = setting.clients.all()
#     print(mailing_clients)
#     for client in mailing_clients:
#         message = setting.message
#         try:
#             send_mail(
#                 subject=message.subject,
#                 message=message.body,
#                 from_email=settings.EMAIL_HOST_USER,
#                 recipient_list=[client.email]
#             )
#             server_respond = 'success'
#             print(f'Рассылка успешно отправлена')
#             # Создание записи в логе рассылки
#             MailingLog.objects.create(
#                 clients=client,
#                 mailing_setting=setting,
#                 attempt_datetime=now(),
#                 server_response=server_respond,
#                 status='C'
#             )
#         except SMTPException as msg:
#             server_respond = f'error code: {msg}'
#             print(server_respond)
#             # Создание записи в логе рассылки
#             MailingLog.objects.create(
#                 clients=client,
#                 mailing_setting=setting,
#                 attempt_datetime=now(),
#                 server_response=server_respond,
#                 status='R'
#             )
#         setting.set_status(status='N', time_last_mailing=now())
#
#
# def send_mailing():
#     mailing_settings = MailingSetting.objects.all()
#     for setting in mailing_settings:
#         time_now = now()
#         # print(now())
#         # print(setting.time_start <= time_now <= setting.time_end and setting.status == 'N')
#         if setting.time_start <= time_now <= setting.time_end and setting.status == 'N':
#             last_try_date = setting.time_last_mailing
#             setting.set_status(status='R', time_last_mailing=time_now)
#
#             delta_time = (time_now - last_try_date).days
#             if delta_time >= 30 and setting.frequency == 'M':
#                 send_message(setting)
#             elif delta_time >= 7 and setting.frequency == 'W':
#                 send_message(setting)
#             elif delta_time >= 1 and setting.frequency == 'D':
#                 send_message(setting)
#             else:
#                 setting.set_status(status='N', time_last_mailing=time_now)
#         elif time_now >= setting.time_end:
#             setting.status = 'N'