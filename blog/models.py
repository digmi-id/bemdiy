import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Kategori(models.Model):
    nama = models.CharField(max_length=32)
    slug = models.SlugField(max_length=250, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Kategori"
        ordering = (
            'created_at',
            'updated_at',
        )

    def __str__(self):
        return self.nama

    def _get_unique_slug(self):
        slug = slugify(self.nama)
        unique_slug = slug
        num = 1
        while Kategori.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug
 
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save()

class Tag(models.Model):
    nama = models.CharField(max_length=32, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Tag"
        ordering = (
            'created_at',
            'updated_at',
        )

    def __str__(self):
        return self.nama

class Artikel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    judul = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    sinopsis = models.TextField()
    isi = models.TextField()
    kategori = models.ForeignKey(Kategori, on_delete=models.SET_NULL, blank=True, null=True)
    tags = models.ManyToManyField(Tag)
    gambar = models.ImageField()
    tanggal_terbit = models.DateTimeField('tanggal terbit')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Artikel"
        ordering = (
            'created_at',
            'updated_at',
        )

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.tanggal_terbit <= now

    was_published_recently.admin_order_field = 'Tanggal diterbitkan'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Telah diterbitkan?'

    def __str__(self):
        return self.judul
    
    def _get_unique_slug(self):
        slug = slugify(self.judul)
        unique_slug = slug
        num = 1
        while Artikel.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug
 
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save()

class Video(models.Model):
    judul = models.CharField(max_length=250, unique=True)
    deskripsi_singkat = models.TextField()
    url = models.URLField(unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Video"
        ordering = (
            'created_at',
            'updated_at',
        )

    def __str__(self):
        return self.judul
