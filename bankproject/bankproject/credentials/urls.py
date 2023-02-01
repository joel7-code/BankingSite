from . import views
from django.urls import path

urlpatterns = [

    path('register',views.register,name='register'),
    path('login', views.login, name='login'),
    path('logout',views.logout,name='logout'),
    path('forms',views.forms,name='forms'),
    path('details',views.details,name='details'),
    path('message',views.message,name='message'),
    path('home', views.home, name='home'),
]