from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Kategori, Tag, Artikel, Video

class KategoriAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nama',) }
    list_display = ('nama', 'slug')
    list_filter = ['nama']
    search_fields = ['nama']
    list_per_page = 25

class TagAdmin(admin.ModelAdmin):
    list_display = ('nama', )
    list_filter = ['nama']
    search_fields = ['nama']
    list_per_page = 25

class VideoAdmin(admin.ModelAdmin):
    list_display = ('judul', 'url')
    list_filter = ['judul']
    search_fields = ['judul']
    list_per_page = 25

class ArtikelAdmin(SummernoteModelAdmin):
    fieldsets = [
        (None,                  {'fields': ['user', 'judul', 'slug', 'sinopsis', 'isi', 'kategori', 'tags', 'gambar']}),
        ('Informasi tanggal',   {'fields': ['tanggal_terbit']}),
    ]
    prepopulated_fields = {'slug': ('judul',) }
    summernote_fields = ('isi', )
    list_display = ('judul', 'kategori', 'user', 'tanggal_terbit', 'was_published_recently')
    list_filter = ['tanggal_terbit']
    search_fields = ['judul']
    list_per_page = 20

admin.site.register(Kategori, KategoriAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Artikel, ArtikelAdmin)
admin.site.register(Video, VideoAdmin)