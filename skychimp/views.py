from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import Permission
from django.http import Http404
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


@login_required
def setting_list(request):
    settings = MailingSetting.objects.all()
    context = {'mailingsetting_list': settings}
    return render(request, 'skychimp/mailingsetting_list.html', context)


@login_required
def message_list(request):
    messages = Message.objects.all()
    context = {'message_list': messages}
    return render(request, 'skychimp/message_list.html', context)


class ClientCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('users:login')
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('skychimp:list-client')

    # def get_queryset(self):
    #     return super().get_queryset().filter(user=self.request.user)


class ClientListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('users:login')
    model = Client

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        if user.is_staff:
            return queryset
        else:
            return queryset.filter(user=user)


class ClientDetailView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('users:login')
    model = Client
    form_class = ClientForm

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('users:login')
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('skychimp:list-client')

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('users:login')
    model = Client
    success_url = reverse_lazy('skychimp:list-client')

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class MailingSettingListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('users:login')
    model = MailingSetting

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        if user.is_staff:
            return queryset
        else:
            return queryset.filter(user=user)

    # def get_context_data(self, *args, **kwargs):
    #
    #     context_data = super().get_context_data(*args, **kwargs)
    #     client_item = Client.objects.get(pk=self.kwargs.get('pk'))
    #     context_data['client_pk'] = client_item.pk
    #     context_data['title'] = f'{client_item.email}'
    #
    #     return context_data


# class IsOwner(Permission):
#     def has_permission(self):
#         print(self)
#         return False


class MailingSettingDetailView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('users:login')
    model = MailingSetting
    form_class = MailingSettingForm
    # permission_classes = [IsOwner]
    permission_required = 'skychimp.is_owner'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.user != self.request.user and not self.request.user.is_staff:
            raise Http404
        return self.object


class MailingSettingCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('users:login')
    model = MailingSetting
    form_class = MailingSettingForm
    success_url = reverse_lazy('skychimp:mailingsetting-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class MailingSettingUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('users:login')
    model = MailingSetting
    form_class = MailingSettingForm
    success_url = reverse_lazy('skychimp:mailingsetting-list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.user != self.request.user:
            raise Http404
        return self.object

    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     return super().form_valid(form)


class MailingSettingDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('users:login')
    model = MailingSetting
    success_url = reverse_lazy('skychimp:mailingsetting-list')


class MessageListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('users:login')
    model = Message

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        if user.is_staff:
            return queryset
        else:
            return queryset.filter(user=user)


class MessageCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('users:login')
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('skychimp:message-list')


class MessageDetailView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('users:login')
    model = Message
    form_class = MessageForm

    # def get_object(self, queryset=None):
    #     self.object = super().get_object(queryset)
    #     if self.object.user != self.request.user and self.request.user != self.object.user.is_staff:
    #         raise Http404
    #     return self.object


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('users:login')
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('skychimp:message-list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.user != self.request.user and self.request.user != self.object.user.is_staff:
            raise Http404
        return self.object


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('users:login')
    model = Message
    success_url = reverse_lazy('skychimp:message-list')