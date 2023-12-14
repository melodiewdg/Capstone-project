from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Booking, Menu
from .serializers import MenuSerializer, BookingSerializer
from rest_framework import generics
from rest_framework import viewsets

# Create your views here.
class MenuItemsView(generics.ListCreateAPIView):
    queryset=Menu.objects.all()
    serializer_class=MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset=Menu.objects.all()
    serializer_class=MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset=Booking.objects.all()
    serializer_class=BookingSerializer