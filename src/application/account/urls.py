from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
    path('',login_view),
    path('login/',login_view),
    path('logout/',logout_view),
    path('changePass/',changePass_view),
]
