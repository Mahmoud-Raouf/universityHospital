# Generated by Django 4.2.11 on 2024-04-19 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_profile_address_profile_birth_date_profile_details_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='file_no',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='رقم الملف'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='postal_code',
            field=models.IntegerField(default=0, verbose_name='postalCode'),
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='تاريخ الحجز')),
                ('time', models.TimeField(verbose_name='الميعاد')),
                ('name', models.CharField(max_length=50, verbose_name='الطبيب :')),
                ('description', models.TextField(max_length=500, verbose_name='ملاحظات')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile', verbose_name='Profile')),
            ],
        ),
    ]
