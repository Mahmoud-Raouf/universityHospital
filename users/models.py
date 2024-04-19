from random import randint
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from django.db.models.signals import post_save


class Profile(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    user = models.OneToOneField(User, verbose_name="User", on_delete=models.CASCADE)
    name = models.CharField("الإسم رباعى", max_length=50)
    mobile_no = models.CharField("رقم الجوال", max_length=50)
    gender = models.CharField('نوع المستخدم', choices=GENDER_CHOICES, default='Male', max_length=50, blank=True, null=True)
    birth_date = models.DateField("تاريخ الميلاد" ,  blank=True, null=True)
    height = models.IntegerField("الطول" ,  blank=True, null=True)
    weight = models.IntegerField("الوزن" ,  blank=True, null=True)
    postal_code = models.IntegerField("postalCode", default=0)
    file_no = models.IntegerField("رقم الملف" ,default=0, blank=True, null=True)
    address = models.CharField("المدينة", max_length=50, blank=True, null=True)
    details = models.TextField("تفاصيل أخرى", max_length=500, blank=True, null=True)
    image = models.ImageField("الصورة الشخصية", upload_to='user-image', blank=True, null=True)
    slug = models.SlugField("Slug", allow_unicode=True, blank=True, null=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.file_no:
            self.file_no = randint(10000, 99999)  # Generate a random number between 10000 and 99999
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        super(Profile, self).save(*args, **kwargs)

def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


post_save.connect(create_profile, sender=User)


class Appointment(models.Model):
    profile = models.ForeignKey(Profile, verbose_name="Profile", on_delete=models.CASCADE)
    date = models.DateField("تاريخ الحجز")
    time = models.TimeField("الميعاد")
    nameDoctor = models.CharField("الطبيب :", max_length=50)
    section = models.CharField("القسم :", max_length=50)
    description = models.TextField("ملاحظات", max_length=500)

    def __str__(self):
        return f"Appointment for {self.profile.name} on {self.date} at {self.time}"
