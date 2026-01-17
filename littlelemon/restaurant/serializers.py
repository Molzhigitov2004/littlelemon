from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Booking, MenuTable

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['name', 'no_of_quests', 'booking_date']

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuTable
        fields = ['title', 'price', 'inventory']
