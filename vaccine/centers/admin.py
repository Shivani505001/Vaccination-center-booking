from django.contrib import admin

# Register your models here.
from .models import VaccineCenter,Booking

admin.site.register(VaccineCenter)
admin.site.register(Booking)
#admin.site.register(Slots)
