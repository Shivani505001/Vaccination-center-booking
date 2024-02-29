from django.urls import path, include 
from . import views
from .views import home

urlpatterns = [
   path('',views.frontpage, name='frontpage'),
   path('home/',views.home, name='home'),
   path('search/',views.search, name='search'),
   #path('pick-a-date/', views.pick_date, name='pick-a-date-without-center'),
   path('pick-a-date/<int:center_id>/', views.pick_date, name='pick-a-date'),
   path('bookings/', views.booking, name='booking'),
]