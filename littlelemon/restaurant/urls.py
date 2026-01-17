from django.contrib import admin 
from django.urls import path 
from . import views
  
urlpatterns = [ 
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('tables', views.BookingView.as_view()),
    path('tables/<int:pk>', views.SingleBookingView.as_view()),
]