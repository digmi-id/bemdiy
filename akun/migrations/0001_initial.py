# Generated by Django 2.0.3 on 2018-04-03 07:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfilPengguna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('divisi', models.CharField(choices=[('AKS', 'Aksi dan Advokasi'), ('EKO', 'Ekonomi'), ('SOS', 'Sosial Kemasyarakatan'), ('PEN', 'Pendidikan dan kebudayaan'), ('POL', 'Politik dan Hukum'), ('PER', 'Pers'), ('KEA', 'Keagamaan'), ('KEP', 'Keperempuanan'), ('KES', 'Kesehatan')], max_length=3)),
                ('nama_lengkap', models.CharField(max_length=100)),
                ('jenis_kelamin', models.CharField(choices=[('P', 'Pria'), ('W', 'Wanita')], default='P', max_length=1)),
                ('nomor_handphone', models.CharField(max_length=13)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created_at', 'updated_at'),
            },
        ),
    ]
