from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model

from ecommerce.accounts.forms import UserRegisterForm, UserUpdateForm
from ecommerce.accounts.models import Profile

UserModel = get_user_model()


@admin.register(UserModel)
class EcommerceUserAdmin(auth_admin.UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2'),
            },
        ),
    )
    model = UserModel
    form = UserUpdateForm
    add_form = UserRegisterForm
    list_display = ('pk', 'email', 'is_staff', 'is_superuser', 'is_active')
    search_fields = ('email',)
    ordering = ('email',)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('pk', 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name')
    ordering = ('first_name', 'last_name')
