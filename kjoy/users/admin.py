from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import *

User = get_user_model()


@admin.register(User)
class UserAdmin(UserAdmin):
    pass


class AccountInline(admin.StackedInline):
    model = Account
    can_delete = False
    verbose_name = 'Профиль'
    verbose_name_plural = 'Профили'


class CustomizedUserAdmin(UserAdmin):
    inlines = (AccountInline, )

admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin)
admin.site.register(Account)