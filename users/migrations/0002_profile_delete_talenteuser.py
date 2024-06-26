# Generated by Django 4.0 on 2024-04-19 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='الإسم رباعى')),
                ('mobile_no', models.CharField(max_length=50, verbose_name='رقم الجوال')),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=50, null=True, verbose_name='نوع المستخدم')),
                ('birth_date', models.DateField(verbose_name='تاريخ الميلاد')),
                ('height', models.IntegerField(verbose_name='الطول')),
                ('weight', models.IntegerField(verbose_name='الوزن')),
                ('postal_code', models.IntegerField(verbose_name='postalCode')),
                ('file_no', models.IntegerField(verbose_name='قم الملف')),
                ('address', models.CharField(blank=True, max_length=50, null=True, verbose_name='المدينة')),
                ('details', models.TextField(blank=True, max_length=500, null=True, verbose_name='تفاصيل أخرى')),
                ('image', models.ImageField(blank=True, null=True, upload_to='user-image', verbose_name='الصورة الشخصية')),
                ('slug', models.SlugField(allow_unicode=True, blank=True, null=True, verbose_name='Slug')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user', verbose_name='User')),
            ],
        ),
        migrations.DeleteModel(
            name='TalenteUser',
        ),
    ]
