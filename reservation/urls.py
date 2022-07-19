from django.urls import path
from . import views

urlpatterns = [
    path('create', views.reservation_create, name="reservation_create"),
    path('details', views.reservation_details, name="reservation_details"),
    path('edit/<res_id>/', views.reservation_edit, name="reservation_edit"),
    path('delete/<res_id>/', views.reservation_delete, name="reservation_delete"),
]
