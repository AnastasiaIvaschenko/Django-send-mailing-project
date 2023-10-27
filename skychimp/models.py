from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
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
    TIME_CHOICES = (
        ('09:00', '09:00'),
        ('18:00', '18:00'),
    )
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
    clients = models.ManyToManyField(Client, through='Subscription', related_name='mailingsetting')
    time_start = models.CharField(**NULLABLE, max_length=5, choices=TIME_CHOICES, verbose_name='Время начала')
    time_end = models.CharField(**NULLABLE, max_length=5, choices=TIME_CHOICES, verbose_name='Время окончания')
    frequency = models.CharField(max_length=1, choices=FREQUENCY_CHOICES, verbose_name='Периодичность')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name='Статус рассылки')


    def __str__(self):
        return f' Рассылка в {self.time_start} {self.frequency} ({self.get_status_display()})'

    class Meta:
        verbose_name = 'настройка рассылки'
        verbose_name_plural = 'настройка рассылки'


class Message(models.Model):
    mailing_setting = models.ForeignKey(MailingSetting, related_name='messages', on_delete=models.CASCADE)
    subject = models.CharField(max_length=200, verbose_name='Тема сообщения')
    body = models.TextField(verbose_name='Тело сообщения')

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


class MailingLog(models.Model):

    STATUS_CHOICES = (
        ('C', 'Завершена'),
        ('N', 'Создана'),
        ('R', 'Запущена'),
    )

    client = models.ForeignKey(Client, on_delete=models.CASCADE, default=None)
    mailing_setting = models.ForeignKey(MailingSetting, related_name='logs', on_delete=models.CASCADE)
    attempt_datetime = models.DateTimeField(verbose_name='Дата и время последней попытки')
    server_response = models.TextField(verbose_name='Ответ почтового сервера', blank=True, null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    def __str__(self):
        return f'Лог рассылки для {self.mailing_setting}'

    class Meta:
        verbose_name = 'попытка рассылки'
        verbose_name_plural = 'попытки рассылки'


class Subscription(models.Model):
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    mailing_setting = models.ForeignKey(MailingSetting, on_delete=models.DO_NOTHING)
    subscribed_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.client} - {self.mailing_setting}'

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'
