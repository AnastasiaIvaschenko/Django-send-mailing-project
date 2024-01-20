from django.contrib import admin

from users.models import User

# admin.site.register(User)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'email', 'phone', 'avatar', 'is_active', 'activation_token',)