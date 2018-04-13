from django.db import models

class ProfilOrganisasi(models.Model):
    nama = models.CharField(max_length=100)
    profil_singkat = models.TextField()
    profil_lengkap = models.TextField()
    visi = models.TextField()
    misi = models.TextField()
    alamat_lengkap = models.TextField()
    alamat_singkat = models.CharField(max_length=100)
    nomor_handphone = models.CharField(max_length=13)
    email = models.EmailField()
    website = models.URLField()
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

class Galeri(models.Model):
    judul = models.CharField(max_length=200)
    deskripsi_singkat = models.CharField(max_length=200)
    gambar = models.ImageField()
    banner = models.BooleanField(default=False, help_text="Apakah gambar ini akan dijadikan sebagai banner?")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = (
            'created_at',
            'updated_at',
        )

    def __str__(self):
        return self.judul


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