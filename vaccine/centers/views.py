from django.shortcuts import render,redirect
from .models import VaccineCenter,Booking
from django.http import HttpResponseNotFound
import datetime
from django.contrib.auth.decorators import login_required
# Create your views here.

def frontpage(request):
    return render(request, 'centers/frontpage.html')
@login_required
def home(request):
    centers_with_slots = []
    centers=VaccineCenter.objects.all()
    
    for center in centers:
        #printing all the available centers with capacity <10 on that particular day
        if Booking.objects.filter(center=center, booking_date=datetime.date.today()).count() < 10:
            centers_with_slots.append(center)
    
    if request.method == "GET":
        #print("In get method")
        today = datetime.datetime.now()
        dates = []
        for i in range(7):
            current_date = today + datetime.timedelta(days=i)
            formatted_date = current_date.strftime("%Y-%m-%d")
            dates.append(formatted_date)
        #print("dates: ", dates)
        # return render(request, 'centers/dateSelection.html', {'dates': dates, "center_id": center_id})
    return render(request, 'centers/home.html', {'centers':centers_with_slots,'dates': dates})
@login_required
def search(request):
    centers = []
    searched = ''
    
    # if request.method == 'POST':
    searched = request.GET.get('search', '')  # Get the search query
    centers = VaccineCenter.objects.filter(name__icontains=searched)
        
    return render(request, 'centers/search.html', {'searched': searched, 'centers': centers})

@login_required
def pick_date(request, center_id=0):
    # TODO: Add the session verification
    
    if request.method == "POST":
        if "center_id" in request.POST:
            center_id = request.POST["center_id"]
        date =request.POST["date"]
        center = VaccineCenter.objects.get(pk=center_id)
        Booking.objects.create(user=request.user, center=center,booking_date=date)
        booked=Booking.objects.filter(center=center,booking_date=date).count()
        rem_capacity=10-booked;
        context={
            'date':date,
            'center':center,
            'rem_capacity':rem_capacity,
            'des':center.description
        }
        return render(request, 'centers/confirm.html', context)
@login_required   
def booking(request, center_id=0):
    if request.method == "GET":
        if "center_id" in request.GET:
            center_id = request.GET["center_id"]
        #center = VaccineCenter.objects.get(pk=center_id)
        booked_centers = Booking.objects.filter(user=request.user)
        print(booked_centers)
        return render(request, 'centers/bookings.html', {'center': booked_centers})
        
        