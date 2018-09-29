from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Kot

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['first_name', 'last_name', 'kot' ,'treasurer']

    fieldsets = UserAdmin.fieldsets + (
            ('My fields', {'fields': ('treasurer', 'internal', 'kot')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Kot)
