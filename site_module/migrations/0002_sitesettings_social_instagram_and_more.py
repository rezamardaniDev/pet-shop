# Generated by Django 4.2.3 on 2023-09-08 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_module', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='social_instagram',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='اینستاگرام'),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='social_telegram',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='تلگرام'),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='social_whatsapp',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='واتس آپ'),
        ),
    ]
