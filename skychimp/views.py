from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from skychimp.forms import ClientForm, MailingSettingForm, MessageForm
from skychimp.models import Client, MailingSetting, Message, MailingLog


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
    login_url = reverse_lazy('users:login')
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('skychimp:list-client')


class ClientListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('users:login')
    model = Client


class ClientDetailView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('users:login')
    model = Client
    form_class = ClientForm


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('users:login')
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('skychimp:list-client')


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('users:login')
    model = Client
    success_url = reverse_lazy('skychimp:list-client')


class MailingSettingListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('users:login')
    model = MailingSetting


class MailingSettingDetailView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('users:login')
    model = MailingSetting
    form_class = MailingSettingForm


class MailingSettingCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('users:login')
    model = MailingSetting
    form_class = MailingSettingForm
    success_url = reverse_lazy('skychimp:mailingsetting-list')


class MailingSettingUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('users:login')
    model = MailingSetting
    form_class = MailingSettingForm
    success_url = reverse_lazy('skychimp:mailingsetting-list')


class MailingSettingDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('users:login')
    model = MailingSetting
    success_url = reverse_lazy('skychimp:mailingsetting-list')


class MessageListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('users:login')
    model = Message


class MessageCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('users:login')
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('skychimp:message-list')


class MessageDetailView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('users:login')
    model = Message
    form_class = MessageForm


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('users:login')
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('skychimp:message-list')


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('users:login')
    model = Message
    success_url = reverse_lazy('skychimp:message-list')