from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    pat('', views.index, name="home")
]