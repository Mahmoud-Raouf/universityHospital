# Generated by Django 4.2.11 on 2024-04-19 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_delete_talenteuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='file_no',
            field=models.IntegerField(blank=True, null=True, verbose_name='رقم الملف'),
        ),
    ]