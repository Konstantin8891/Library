from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin, Group

from .models import CustomUser
from .forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = (
        "id",
        "username",
        "first_name",
        "last_name",
        "email",
        "organization_id"
    )
    list_filter = ('first_name', 'last_name', 'username', 'email')
    fieldsets = (
        (None, {'fields': (
            'email',
            'username',
            'first_name',
            'last_name',
            'organization_id',
            'password'
        )}),
        ('Permissions', {'fields': ('is_admin', 'is_staff')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'username',
                'first_name',
                'last_name',
                'organization_id',
                'password1',
                'password2'
            ),
        }),
    )
    search_fields = ('email', 'first_name', 'last_name', 'username')
    ordering = ('id',)
    filter_horizontal = ()


admin.site.register(CustomUser, UserAdmin)
admin.site.unregister(Group)
