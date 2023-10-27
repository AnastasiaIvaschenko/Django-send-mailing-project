from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from skychimp.forms import ClientForm, MailingSettingForm, MessageForm
from skychimp.models import Client, MailingSetting, Message, MailingLog, Subscription


def index(request):
    context = {
        'object_list': Client.objects.all(),
        'title': 'Главная'
    }
    return render(request, 'skychimp/base.html', context)


def setting_list(request):
    settings = MailingSetting.objects.all()
    context = {'mailingsetting_list': settings}
    return render(request, 'skychimp/mailingsetting_list.html', context)


def message_list(request):
    messages = Message.objects.all()
    context = {'message_list': messages}
    return render(request, 'skychimp/message_list.html', context)


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('skychimp:list-client')


class ClientListView(LoginRequiredMixin, ListView):
    model = Client


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    form_class = ClientForm


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('skychimp:list-client')


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('skychimp:list-client')


class MailingSettingListView(LoginRequiredMixin, ListView):
    model = MailingSetting


class MailingSettingDetailView(LoginRequiredMixin, DetailView):
    model = MailingSetting
    form_class = MailingSettingForm


class MailingSettingCreateView(LoginRequiredMixin, CreateView):
    model = MailingSetting
    form_class = MailingSettingForm
    success_url = reverse_lazy('skychimp:mailingsetting-list')


class MailingSettingUpdateView(LoginRequiredMixin, UpdateView):
    model = MailingSetting
    form_class = MailingSettingForm
    success_url = reverse_lazy('skychimp:mailingsetting-list')


class MailingSettingDeleteView(LoginRequiredMixin, DeleteView):
    model = MailingSetting
    success_url = reverse_lazy('skychimp:mailingsetting-list')


class MessageListView(LoginRequiredMixin, ListView):
    model = Message


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('skychimp:message-list')


class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message
    form_class = MessageForm


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('skychimp:message-list')


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    success_url = reverse_lazy('skychimp:message-list')