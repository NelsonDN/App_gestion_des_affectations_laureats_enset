from django.urls import path
from . import views


app_name = "gestionadmin"

urlpatterns = [
    path('', views.home, name = 'home'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('profile/', views.profile, name = 'profile'),
]

