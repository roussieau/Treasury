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


def the_interns_eat(modeladmin, request, queryset):
    for kot in queryset:
        kot.the_interns_eat()
the_interns_eat.short_description = "Enregistrer les internes à tous les soupers par défaut"

class KotAdmin(admin.ModelAdmin):
    actions = [the_interns_eat]


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Kot, KotAdmin)
