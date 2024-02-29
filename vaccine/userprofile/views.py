from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required,permission_required
from .models import userprofile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from centers.form import ProductForm
from centers.models import VaccineCenter,Booking
from django.shortcuts import get_object_or_404
from django.db.models import Sum

# Create your views here.

@login_required
@permission_required('centers.can_add_center', raise_exception=True)
def admin_details(request):
    centers = VaccineCenter.objects.all()
    return render(request, 'userprofile/admin/admin_details.html', {'centers': centers})

@login_required
@permission_required('centers.can_add_center',raise_exception=True)
def add_center(request):
    if request.method=='POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_details')
    else:
        form=ProductForm()
        
    return render(request,'userprofile/admin/add_center.html',{'form':form})

@login_required
@permission_required('centers.can_delete_center',raise_exception=True)
def delete_center(request, center_id):
    center = get_object_or_404(VaccineCenter, pk=center_id)
    
    if request.method == 'POST':
        center.delete()
        return redirect('admin_details')
    
    return render(request, 'userprofile/admin/delete.html', {'center': center})
@login_required
@permission_required('centers.can_add_center',raise_exception=True)
def dosage_details(request):
    # Aggregate dosage details grouped by center and date
    dosage_details = Booking.objects.values('center__name', 'booking_date').annotate(total_dosage=Sum('dosage'))
    return render(request, 'userprofile/admin/dosage.html', {'dosage_details': dosage_details})

def signup(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        
        if form.is_valid():
            user=form.save()
        
            login(request,user) 
        #To log a user in, from a view, use login(). It takes an HttpRequest object and a User object. login() saves the user’s ID in the session, using Django’s session framework.
            Userprofile= userprofile.objects.create(user=user)#creating a new instance of userprofile
            return redirect('myaccount')
    else:
        form=UserCreationForm()
    return render(request,'userprofile/signup.html',{'form':form})

@login_required
def myaccount(request):
    return render(request,'userprofile/myaccount.html')

