from django.contrib import admin
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('',views.home, name='home'),
    path('login/',views.login_view, name='login'),
    path('register/',views.register_view, name='register'),
    path('logout/',views.logout_view, name='logout'),
    path('profile/',views.profile_view, name='profile-view'),
   # path('profile/<int:profile_id>', views.profile_detail, name='profile-detail'),
    path('profile/edit/',views.profile_edit, name='profile-edit'),
    path('change-password/',views.password_change,name='password-change'),

]