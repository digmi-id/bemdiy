from django.contrib import admin

from .models import ProfilOrganisasi, SosialMedia

class SosialMediaInline(admin.TabularInline):
    model = SosialMedia
    extra = 0

class ProfilOrganisasiAdmin(admin.ModelAdmin):
    inlines = [SosialMediaInline]
    list_display = ('nama', 'email', 'nomor_handphone')
    list_per_page = 1


admin.site.register(ProfilOrganisasi, ProfilOrganisasiAdmin)
