from photo.models import Photographer , Style
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from photo.forms import UserChangeForm, UserCreationForm


class UserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm


    list_display = ('email', 'username', 'is_admin',)
    list_filter = ('is_admin',) 
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Personal info', {'fields': ('date_birth', 'first_name', 'second_name','sity')}),
        ('Permissions', {'fields': ('is_admin',)}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(Photographer, UserAdmin)
admin.site.unregister(Group)