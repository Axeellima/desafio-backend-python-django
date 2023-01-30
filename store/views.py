from django.shortcuts import render

from .models import Store
from .serializers import StoreSerializer

from rest_framework.generics import ListAPIView
# Create your views here.
class StoreView(ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer