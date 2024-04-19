from django.urls import path
from . import views
app_name = 'users'

urlpatterns = [
    path('signup/' , views.signup, name='signup'),
    path('login/' , views.user_login, name='login'),
    path('logout/' , views.logout, name='logout'),
    path('profile/' , views.profile , name='profile'),


    # path('update/talente/' , views.update_talente, name='update_talente'),
    # path('create/talente/' , views.create_talente, name='create_talente'),
    path('change_password/' , views.change_password , name = 'change_password'),


]