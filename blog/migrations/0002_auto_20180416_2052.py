# Generated by Django 2.0.3 on 2018-04-16 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='url',
            field=models.URLField(unique=True),
        ),
    ]
