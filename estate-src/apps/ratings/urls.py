from django.urls import path
from . import views

urlpatterns = [
    # Userauths API Endpoints
    path('<str:profile_id>/', views.create_agent_review, name='create-rating'),
    
]