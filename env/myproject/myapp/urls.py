"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('appoinment',views.appoinment,name='appoinment'),
    path('contact',views.contact,name='contact'),
    path('department',views.department,name='department'),
    path('drlist',views.drlist,name='drlist'),
    path('registration',views.registration,name='registration'),
    path('drregister',views.drregister,name='drregister'),
    path('login', views.login, name='login'),
    path('deptregistration', views.deptregistration, name='deptregistration'),
    path('adminmodule', views.adminmodule, name='adminmodule'),
    path('drmodule', views.drmodule, name='drmodule'),
    path('adminapprove', views.adminapprove, name='adminapprove'),
    path('viewpatient',views.viewpatient,name='viewpatient'),
    path('usermodule',views.usermodule,name='usermodule'),
    path('signup',views.signup,name='signup'),


]
