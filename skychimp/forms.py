from django import forms
from skychimp.models import Client, MailingSetting, Message, MailingLog
from django.core.exceptions import ValidationError


class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = '__all__'


class MailingSettingForm(forms.ModelForm):
    clients = forms.ModelMultipleChoiceField(queryset=Client.objects.all(), widget=forms.CheckboxSelectMultiple,
                                             label='Выберите клиентов')

    class Meta:
        model = MailingSetting
        fields = '__all__'


class MessageForm(forms.ModelForm):
    mailing_setting = forms.ModelChoiceField(queryset=MailingSetting.objects.all())

    class Meta:
        model = Message
        fields = ['mailing_setting', 'subject', 'body']

