import datetime
from django.db import models
from django.utils import timezone

from akun.models import ProfilPengguna

class Artikel(models.Model):
    user = models.ForeignKey(ProfilPengguna, on_delete=models.CASCADE)
    judul = models.CharField(max_length=250)
    isi = models.TextField()
    gambar = models.ImageField()
    tanggal_terbit = models.DateTimeField('tanggal terbit')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
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
