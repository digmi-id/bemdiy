from django.db import models

class ProfilOrganisasi(models.Model):
    nama = models.CharField(max_length=100)
    alamat_lengkap = models.TextField()
    alamat_singkat = models.CharField(max_length=100)
    nomor_handphone = models.CharField(max_length=13)
    email = models.EmailField()
    logo = models.ImageField()
    favicon = models.ImageField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = (
            'created_at',
            'updated_at',
        )

    def __str__(self):
        return self.nama

class SosialMedia(models.Model):
    profil = models.ForeignKey(ProfilOrganisasi, on_delete=models.CASCADE)
    nama = models.CharField(max_length=200)
    url = models.URLField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = (
            'created_at',
            'updated_at',
        )

    def __str__(self):
        return self.nama