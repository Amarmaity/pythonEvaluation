from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    # path('',views.home, name='home'),
    path('super-admin/',views.viewSuperAdminDashboard, name='SuperAdminDashboard'),
    path('add-user/', views.AddUser,name='add_user'),
]
