from django.urls import path
from . import views

urlpatterns = [
    path('', views.AddReservationView.as_view(), name='reservation'),
    path('details/', views.ReservationListView.as_view(), name='reservation_details'),
    path('edit/<pk>/', views.ReservationUpdateView.as_view(), name='reservation_edit'),
    path('delete/<pk>/', views.ReservationDeleteView.as_view(), name='reservation_delete'),
]
