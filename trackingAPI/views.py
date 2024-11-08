from django.shortcuts import render
from rest_framework import generics
from .models import Cryptocurrency
from .serializers import CryptocurrencySerializer

# Create your views here.
class ListCryptocurrencyView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Cryptocurrency.objects.all()
    serializer_class = CryptocurrencySerializer
    
def home(request):
    return render(request, 'home.html')