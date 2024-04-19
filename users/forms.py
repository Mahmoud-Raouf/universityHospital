from django import forms
from .models import * 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator



class UserCreationForms(UserCreationForm):

    email        = forms.CharField(label='البريد الالكتروني', )
    password1       = forms.CharField(label='كلمة المرور', widget=forms.PasswordInput() , min_length=8)
    password2       = forms.CharField(label='تأكيد كلمة المرور', widget=forms.PasswordInput() , min_length=8)

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('كلمات المرور غير متطابقة. الرجاء إعادة المحاولة.')

        return cleaned_data
    
    class Meta:
        model = User
        fields = ('username','email', 'password1' , 'password2')

class ProfileForms(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("name", "mobile_no", "gender", "birth_date", "height", "weight", "postal_code", 
                  "address", "details", "image")
        labels = {
            'name': 'الإسم رباعى',
            'mobile_no': 'رقم الجوال',
            'gender': 'نوع المستخدم',
            'birth_date': 'تاريخ الميلاد',
            'height': 'الطول',
            'weight': 'الوزن',
            'postal_code': 'postalCode',
            'file_no': 'رقم الملف',
            'address': 'المدينة',
            'details': 'تفاصيل أخرى',
            'image': 'الصورة الشخصية',
        }
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }


# class AppointmentForm(forms.ModelForm):
#     class Meta:
#         model = Appointment
#         fields = ("date" , "time" , "name" , "description")


#     def clean(self):
#         cleaned_data = super().clean()
#         name = cleaned_data.get('name')
#         mobileNo = cleaned_data.get('mobileNo')
#         address = cleaned_data.get('address')

#         if not mobileNo or not str(mobileNo).isdigit():
#             self.add_error('mobileNo', 'يجب أن يكون رقم الهاتف عبارة عن أرقام فقط.')

#         return cleaned_data
    
# class CompanyForms(forms.ModelForm):
#     class Meta:
#         model = Company
#         fields = ("name", "mobileNo", "licenseNo","classification_certificate",
#                    "description", "services",
#                   "image" ,)

#     def clean(self):
#         cleaned_data = super().clean()
#         name = cleaned_data.get('name')
#         mobileNo = cleaned_data.get('mobileNo')
#         address = cleaned_data.get('address')

#         if not mobileNo or not str(mobileNo).isdigit():
#             self.add_error('mobileNo', 'يجب أن يكون رقم الهاتف عبارة عن أرقام فقط.')

#         return cleaned_data
        
# class TalenteIdeaForm(forms.ModelForm):
#     class Meta:
#         model = TalenteIdea
#         fields = ("company" , "name" ,"description" , "age" ,"address" , "email" ,"field" ,)
        
class UserForm(forms.ModelForm):
    username        = forms.CharField(label='البريد الالكتروني', )

    class Meta:
        model = User
        fields = ("username" , "password")



class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username" ,"email")



