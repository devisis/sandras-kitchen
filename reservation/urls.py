from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(views.AddReservationView.as_view()), name='reservation'),
    path('details/', login_required(views.ReservationListView.as_view()), name='reservation_details'),
    path('edit/<pk>/', login_required(views.ReservationUpdateView.as_view()), name='reservation_edit'),
    path('delete/<pk>/', login_required(views.ReservationDeleteView.as_view()), name='reservation_delete'),
]
