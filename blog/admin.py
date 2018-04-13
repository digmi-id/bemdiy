from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Kategori, Tag, Artikel

class KategoriAdmin(admin.ModelAdmin):
    list_display = ('nama', )
    list_filter = ['nama']
    search_fields = ['nama']
    list_per_page = 25

class TagAdmin(admin.ModelAdmin):
    list_display = ('nama', )
    list_filter = ['nama']
    search_fields = ['nama']
    list_per_page = 25

class ArtikelAdmin(SummernoteModelAdmin):
    fieldsets = [
        (None,                  {'fields': ['user', 'judul', 'sinopsis', 'isi', 'kategori', 'tags', 'gambar']}),
        ('Informasi tanggal',   {'fields': ['tanggal_terbit'], 'classes': ['collapse']}),
    ]
    summernote_fields = ('isi', )
    list_display = ('judul', 'tanggal_terbit', 'was_published_recently')
    list_filter = ['tanggal_terbit']
    search_fields = ['judul']
    list_per_page = 3

admin.site.register(Kategori, KategoriAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Artikel, ArtikelAdmin)