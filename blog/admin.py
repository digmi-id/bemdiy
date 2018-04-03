from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Artikel

class ArtikelAdmin(SummernoteModelAdmin):
    fieldsets = [
        (None,                  {'fields': ['user', 'judul', 'isi', 'gambar']}),
        ('Informasi tanggal',   {'fields': ['tanggal_terbit'], 'classes': ['collapse']}),
    ]
    summernote_fields = ('isi', )
    list_display = ('judul', 'tanggal_terbit', 'was_published_recently')
    list_filter = ['tanggal_terbit']
    search_fields = ['judul']
    list_per_page = 3

admin.site.register(Artikel, ArtikelAdmin)