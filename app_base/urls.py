from django.urls import path
from app_base import views

urlpatterns = [
        #inicio carros
    path ('', views.inicio)
]
