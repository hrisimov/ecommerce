from django.contrib import admin
from django.contrib.auth import get_user_model

from ecommerce.accounts.models import Profile

UserModel = get_user_model()


@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'username', 'is_staff', 'is_active')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'first_name', 'last_name')
