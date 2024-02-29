from django.db import models
from django.core.validators import MaxValueValidator
from django.utils import timezone
# Create your models here.

from django.contrib.auth.models import User


class VaccineCenter(models.Model):
    name=models.CharField(max_length=100)
    address=models.TextField()
    phone=models.CharField(max_length=10)
    email=models.EmailField()
    
    starttime=models.TimeField()
    endtime=models.TimeField()
    description=models.TextField(default='')
    capacity=models.PositiveIntegerField(default=10,validators=[MaxValueValidator(10)])
    
    def __str__(self):
        return self.name 
    
class Booking(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    center = models.ForeignKey(VaccineCenter, on_delete=models.CASCADE)
    booking_date = models.DateField(default=timezone.now,null=False, blank=False)  # Date of booking
    dosage=models.IntegerField(default=1) #for each booking dosage is 1 

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        # Check if the booking date already has 10 bookings
        if Booking.objects.filter(booking_date=self.booking_date).count() >= 10:
            raise Exception("Maximum bookings reached for this date.")
        else:
            super().save(*args, **kwargs)


# #permissions

from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

def create_permissions_after_migration(sender, **kwargs):
    content_type = ContentType.objects.get_for_model(VaccineCenter)
    permission = Permission.objects.create(
        codename="can_add_center",
        name="Can add centers",
        content_type=content_type,
    )
# Create permission for deleting centers
    delete_permission = Permission.objects.create(
        codename="can_delete_center",
        name="Can delete centers",
        content_type=content_type,
        )

# Connect post_migrate signal
from django.db.models.signals import post_migrate
post_migrate.connect(create_permissions_after_migration)