from django.urls import path
from .views import MenuView

app_nam = 'menu'

urlpatterns = [
    path('', MenuView.as_view(), name='menu'),
]
