from django.contrib import admin

from .models import ProfilOrganisasi, SosialMedia, Galeri

class SosialMediaInline(admin.TabularInline):
    model = SosialMedia
    extra = 0

class ProfilOrganisasiAdmin(admin.ModelAdmin):
    inlines = [SosialMediaInline]
    list_display = ('nama', 'email', 'nomor_handphone')
    list_per_page = 1

class GaleriAdmin(admin.ModelAdmin):
    list_display = ('judul', 'deskripsi_singkat')
    list_filter = ['judul']
    search_fields = ['judul']
    list_per_page = 25

admin.site.register(ProfilOrganisasi, ProfilOrganisasiAdmin)
admin.site.register(Galeri, GaleriAdmin)
