from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import CustomUser

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username',)
    # list_filter = ('created', 'status')
    # search_fields = ('name', 'surname', 'patronymic', 'phone')
    # readonly_fields = ('created',)
    # add_form = CustomUserCreationForm
    # form = CustomUserChangeForm
    # model = CustomUser
    # list_display = ['email', 'username',]


admin.site.unregister(Group)
