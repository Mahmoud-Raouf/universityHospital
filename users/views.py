from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

# from company.models import Opportunity
from .forms import *
from django.contrib.auth import authenticate , login
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib import auth
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm



def signup(request):
    if request.method == 'POST':
        user_form = UserCreationForms(request.POST)
        profile_form = ProfileForms(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = request.user
            profile.save()

            username = user_form.cleaned_data.get('username')
            password = user_form.cleaned_data.get('password2')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'تم إنشاء المستخدم والشركة بنجاح.')
                return redirect('users:profile')  

    else:
        user_form = UserCreationForms()
        profile_form = ProfileForms()

    return render(request, 'registration/signup.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })


# def AppointmentCreate(request):
#     user = request.user

#     profile = get_object_or_404(Profile, user=user)

#     if request.method == 'POST':
#         form = Profile(request.POST, request.FILES, instance=profile.talenteuser)
#         if form.is_valid():
#             form.save()
#             return redirect('users:profile') 
#     else:
#         form = Profile(instance=profile.talenteuser)
#     return render(request, 'registration/talenteIdea_update.html', {'form': form})


# def update_talente(request):
#     user = request.user

#     profile = get_object_or_404(Profile, user=user)

#     if request.method == 'POST':
#         form = Profile(request.POST, request.FILES, instance=profile.talenteuser)
#         if form.is_valid():
#             form.save()
#             return redirect('users:profile') 
#     else:
#         form = Profile(instance=profile.talenteuser)
#     return render(request, 'registration/talenteIdea_update.html', {'form': form})




def user_login(request):
    if request.method == 'POST':
        login_form = UserForm()

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request , username=username , password=password)
        if user is not None:
            login(request , user)
            return redirect('users:profile')  

        else:
            messages.error(request, ' خطأ فى بيانات الدخول أعد المحاولة')

    else:
        login_form = UserForm()
        
    return render(request , 'registration/login.html' , {
        'login_form' : login_form
    })


def logout(request):
    auth.logout(request)
    return redirect('users:login')


@login_required(login_url='/users/login/')
def profile(request):
    userProfile = Profile.objects.get(user =request.user)
    userAppointment = Appointment.objects.filter(profile =userProfile)
    return render(request , 'profile.html' , {
        'userProfile' : userProfile,
        'userAppointment' : userAppointment,
    })

@login_required(login_url='/user/login/')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('users:profile') 
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {
        'form': form
    })