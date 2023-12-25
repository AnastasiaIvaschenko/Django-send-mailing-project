from django.contrib import admin
from skychimp.models import Client, MailingSetting, Message, MailingLog#, Subscription


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('pk', 'email', 'first_name', 'last_name', 'comment',)
    search_fields = ('email', 'last_name',)


@admin.register(MailingSetting)
class MailingSettingAdmin(admin.ModelAdmin):
    list_display = ('pk', 'time_start', 'time_end', 'frequency', 'status', 'message',)
    list_filter = ('clients', 'frequency', 'message',)
    search_fields = ('status',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'subject', 'body',)
    search_fields = ('subject',)


@admin.register(MailingLog)
class MailingLogAdmin(admin.ModelAdmin):
    list_display = ('pk', 'mailing_setting', 'attempt_datetime', 'status', 'server_response',)
    list_filter = ('mailing_setting', 'status', 'clients',)
    search_fields = ('attempt_datetime',)


# @admin.register(Subscription)
# class Subscription(admin.ModelAdmin):
#     list_display = ('pk', 'client', 'mailing_setting', 'subscribed_date',)
#     list_filter = ('client', 'mailing_setting',)
#     search_fields = ('subscribed_date',)



