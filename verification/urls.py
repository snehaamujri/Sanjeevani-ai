
from django.urls import path
from . import views

urlpatterns = [
    path('verify/<str:batch_id>/', views.verify_batch, name='verify_batch'),
    path('send-report/', views.send_report, name='send_report'),  # NEW!
]
