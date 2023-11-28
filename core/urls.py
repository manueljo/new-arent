from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('profile/', views.profile, name='profile'),
    path('ussd/', views.ussd, name='ussd'),
    path('apartment/<int:pk>/', views.apartment, name='apartment-detail'),
]
