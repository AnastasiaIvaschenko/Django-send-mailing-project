from random import random

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView

from django.core.mail import send_mail
from django.shortcuts import redirect, render

from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, TemplateView

from config import settings
from users.forms import UserRegisterForm, UserForm
from users.models import User

from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import ObjectDoesNotExist


class LoginView(BaseLoginView):
    template_name = 'users/login.html'


class LogoutView(BaseLogoutView):
    pass


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:register_success')
    template_name = 'users/register.html'

    def form_valid(self, form):
        # Создание пользователя со значением is_active=False
        new_user = form.save(commit=False)
        new_user.is_active = False
        new_user.save()
        # Генерация кода для юзера и запись в БД
        token = default_token_generator.make_token(new_user)
        activation_url = f'http://{get_current_site(self.request).domain}/users/activate/{token}/'
        new_user.activation_token = token
        new_user.save()

        # Отправка электронной почты
        send_mail(
            subject='Поздравляем с регистрацией',
            message=f'Пожалуйста, перейдите по ссылке для активации вашего аккаунта:\n\n{activation_url}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email]
        )
        return super().form_valid(form)


def activate_account(request, activation_token):
    try:
        user = User.objects.get(activation_token=activation_token)
        user.is_active = True
        user.save()
        return redirect(reverse('users:login'))  # Перенаправление на страницу входа
    except (TypeError, ValueError, OverflowError, ObjectDoesNotExist):
        return render(request, 'users/activation_error.html')


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user
    #
    # def get_object(self, queryset=None):
    #     self.object = super().get_object(queryset)
    #     if self.object.user != self.request.user and not self.request.user.is_staff:
    #         raise Http404
    #     return self.object

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     user = self.request.user
    #     if user.is_staff:
    #         return queryset
    #     else:
    #         return queryset.filter(user=user)

def generate_new_password(request):
    new_password = ''.join([str(random.randint(0, 9) for _ in range(12))])
    send_mail(
        subject='Вы сменили пароль',
        message=f'Ваш новый пароль {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email],
    )
    request.user.set_password(new_password)
    request.user.save()
    return redirect(reverse('skychimp:index'))


class RegisterSuccessView(TemplateView):
    template_name = 'users/register_success.html'
