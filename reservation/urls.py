from django.urls import path
from . import views

urlpatterns = [
    path('', views.reservation, name="reservation"),
    path('my_reservations/', views.EditReservations, name="my_reservations"),
]
