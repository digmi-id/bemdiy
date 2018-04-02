from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from akun.models import ProfilPengguna

class ProfilPenggunaInline(admin.StackedInline):
    model = ProfilPengguna
    can_delete = False
    verbose_name_plural = 'Profil Pengguna'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfilPenggunaInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)