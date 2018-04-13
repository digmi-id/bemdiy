from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from akun.models import ProfilPengguna, Devisi

class ProfilPenggunaInline(admin.StackedInline):
    model = ProfilPengguna
    can_delete = False
    verbose_name_plural = 'Profil Pengguna'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfilPenggunaInline, )


class DevisiAdmin(admin.ModelAdmin):
    list_display = ('nama', 'deskripsi', 'icon')
    list_filter = ['nama']
    search_fields = ['nama']
    list_per_page = 25

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Devisi, DevisiAdmin)