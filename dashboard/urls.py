from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.healthworker_dashboard, name='healthworker_dashboard'),
    path('dashboard/download/', views.download_inventory, name='download_inventory'),
]