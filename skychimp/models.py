from django.db import models
from users.models import User


NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='clients', **NULLABLE)
    email = models.EmailField(max_length=100, verbose_name='Контактный email')
    first_name = models.CharField(**NULLABLE, max_length=100, verbose_name='Имя')
    last_name = models.CharField(**NULLABLE, max_length=100, verbose_name='Фамилия')
    comment = models.TextField(**NULLABLE, verbose_name='Комментарий')

    def __str__(self):
        return (f'{self.first_name} {self.last_name} \n '
                f'{self.email}')

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'


class MailingSetting(models.Model):

    FREQUENCY_CHOICES = (
        ('D', 'Раз в день'),
        ('W', 'Раз в неделю'),
        ('M', 'Раз в месяц'),
    )
    STATUS_CHOICES = (
        ('C', 'Завершена'),
        ('N', 'Создана'),
        ('R', 'Запущена'),
    )

    clients = models.ManyToManyField('Client', related_name='mailing_settings')
    time_start = models.DateTimeField(verbose_name='Время начала', **NULLABLE)
    time_end = models.DateTimeField(verbose_name='Время окончания', **NULLABLE)
    frequency = models.CharField(max_length=1, choices=FREQUENCY_CHOICES, verbose_name='Периодичность')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name='Статус рассылки')
    message = models.ForeignKey('Message', related_name='mailing_settings', on_delete=models.CASCADE, **NULLABLE)
    time_last_mailing = models.DateTimeField(**NULLABLE, verbose_name='Дата и Время последней рассылки')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mailing_settings', **NULLABLE)

    def set_status(self, status, time_last_mailing):
        self.time_last_mailing = time_last_mailing
        self.status = status
        self.save()

    def __str__(self):
        return f' Рассылка в {self.time_start} {self.message} {self.frequency} ({self.get_status_display()})'

    class Meta:
        verbose_name = 'настройка рассылки'
        verbose_name_plural = 'настройка рассылки'


class Message(models.Model):
    subject = models.CharField(max_length=200, verbose_name='Тема сообщения')
    body = models.TextField(verbose_name='Тело сообщения')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages', **NULLABLE)

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


class MailingLog(models.Model):
    STATUS_CHOICES = (
        ('C', 'Успешно'),
        ('N', 'Неуспешно'),
    )
    mailing_setting = models.ForeignKey(MailingSetting, related_name='logs', on_delete=models.CASCADE)
    clients = models.ForeignKey(Client, related_name='client', **NULLABLE, on_delete=models.CASCADE)
    attempt_datetime = models.DateTimeField(verbose_name='Дата и время последней попытки')
    server_response = models.TextField(verbose_name='Ответ почтового сервера', blank=True, null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    def __str__(self):
        return f'Лог рассылки для {self.mailing_setting}'

    class Meta:
        verbose_name = 'попытка рассылки'
        verbose_name_plural = 'попытки рассылки'
        permissions = [
            (
                'is_owner',
                'Can view mailingsettings'
            )
        ]


