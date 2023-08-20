# Generated by Django 4.2.3 on 2023-08-19 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog_module', '0011_blogcomment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogcomment',
            options={'verbose_name': 'نظر', 'verbose_name_plural': 'نظرات'},
        ),
        migrations.AlterField(
            model_name='blogcomment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog_module.blog', verbose_name='پست'),
        ),
    ]