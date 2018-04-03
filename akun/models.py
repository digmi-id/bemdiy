from django.db import models
from django.contrib.auth.models import User

class ProfilPengguna(models.Model):
    DIVISI_CHOICES = (
        ("AKS", "Aksi dan Advokasi"),
        ("EKO", "Ekonomi"),
        ("SOS", "Sosial Kemasyarakatan"),
        ("PEN", "Pendidikan dan kebudayaan"),
        ("POL", "Politik dan Hukum"),
        ("PER", "Pers"),
        ("KEA", "Keagamaan"),
        ("KEP", "Keperempuanan"),
        ("KES", "Kesehatan")
    )
    JENIS_KELAMIN_CHOICES = (
        ("P", "Pria"),
        ("W", "Wanita")
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    divisi = models.CharField(max_length=3, choices=DIVISI_CHOICES)
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