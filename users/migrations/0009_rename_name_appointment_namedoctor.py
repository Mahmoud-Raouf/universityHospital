# Generated by Django 4.2.11 on 2024-04-19 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_appointment_section'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='name',
            new_name='nameDoctor',
        ),
    ]