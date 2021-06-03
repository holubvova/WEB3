
from django.contrib import admin
from django.urls import path, include
from fotozone import views
urlpatterns = [

    path('',views.sign, name="sign_in"),
    path('about_site_n/',views.about_n, name="about_n"),
    path('about_site_y/',views.about_y, name="about_y"),
    path('fotozone_n/',views.fotozone_n, name="fotozone_n"),
    path('fotozone_y/',views.fotozone_y, name="fotozone_y"),
    path('edit/', views.edit, name="edit"),
    path ('forgot_password', views.forgot_password, name='forgot_password'),
    path('register/',views.register,name='register'),
    path('profile/',views.profile, name="profile"),
    path('admin/', admin.site.urls)


]
