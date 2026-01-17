from .serializers import MenuItemSerializer, BookingSerializer
from .models import MenuTable, Booking
from rest_framework import generics, viewsets
# Create your views here.

class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuTable.objects.all()
    serializer_class = MenuItemSerializer


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuTable.objects.all()
    serializer_class = MenuItemSerializer

class BookingView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class SingleBookingView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer