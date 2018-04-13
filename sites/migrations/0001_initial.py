# Generated by Django 2.0.3 on 2018-04-13 21:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Galeri',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=200)),
                ('deskripsi_singkat', models.CharField(max_length=200)),
                ('gambar', models.ImageField(upload_to='')),
                ('banner', models.BooleanField(default=False, help_text='Apakah gambar ini akan dijadikan sebagai banner?')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('created_at', 'updated_at'),
            },
        ),
        migrations.CreateModel(
            name='ProfilOrganisasi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('profil_singkat', models.TextField()),
                ('profil_lengkap', models.TextField()),
                ('visi', models.TextField()),
                ('misi', models.TextField()),
                ('alamat_lengkap', models.TextField()),
                ('alamat_singkat', models.CharField(max_length=100)),
                ('nomor_handphone', models.CharField(max_length=13)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.URLField()),
                ('logo', models.ImageField(upload_to='')),
                ('latitude', models.CharField(max_length=100)),
                ('longitude', models.CharField(max_length=100)),
                ('favicon', models.ImageField(upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('created_at', 'updated_at'),
            },
        ),
        migrations.CreateModel(
            name='SosialMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=200)),
                ('url', models.URLField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('profil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.ProfilOrganisasi')),
            ],
            options={
                'ordering': ('created_at', 'updated_at'),
            },
        ),
    ]
