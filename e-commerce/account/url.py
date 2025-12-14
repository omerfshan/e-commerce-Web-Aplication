from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [
    path('login',views.login_request,name="login"),
    path('register',views.register_request,name="register"),
    path('logout',views.logout_request,name="logout"),

   
] 
