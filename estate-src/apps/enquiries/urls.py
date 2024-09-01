from django.urls import path
from . import views

urlpatterns = [
    # Userauths API Endpoints
    path('', views.send_enquiry_email, name='send-enquiry'),
    
]