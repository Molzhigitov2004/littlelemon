from .serializers import MenuItemSerializer
from .models import MenuTable, Booking
from rest_framework import generics
# Create your views here.

class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuTable.objects.all()
    serializer_class = MenuItemSerializer


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuTable.objects.all()
    serializer_class = MenuItemSerializer