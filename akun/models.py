from django.db import models
from django.contrib.auth.models import User

class Devisi(models.Model):
    nama = models.CharField(max_length=200)
    deskripsi = models.TextField()
    icon = models.CharField(
        max_length=20,
        help_text=
        "Untuk melihat daftar icon kunjungi https://fontawesome.com/v4.7.0/icons"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = (
            'created_at',
            'updated_at',
        )

    def __str__(self):
        return self.nama

class ProfilPengguna(models.Model):
    JENIS_KELAMIN_CHOICES = (
        ("P", "Pria"),
        ("W", "Wanita")
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    devisi = models.OneToOneField(Devisi, on_delete=models.CASCADE)
    nama_lengkap = models.CharField(max_length=100)
    jenis_kelamin = models.CharField(max_length=1, default="P", choices=JENIS_KELAMIN_CHOICES)
    nomor_handphone = models.CharField(max_length=13)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = (
            'created_at',
            'updated_at',
        )

    def __str__(self):
        return self.nama_lengkap