from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),  # This makes the homepage accessible at the root URL
]