from django.urls import path
from users.apps import UsersConfig
from users.views import LoginView, LogoutView, RegisterView, UserUpdateView, generate_new_password, RegisterSuccessView, \
    activate_account

from django.conf.urls.static import static
from config import settings

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', UserUpdateView.as_view(), name='profile'),
    path('profile/genpassword/', generate_new_password, name='generate_new_password'),
    path('activate/<slug:activation_token>/', activate_account, name='activate_account'),
    path('register/success/', RegisterSuccessView.as_view(), name='register_success'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)