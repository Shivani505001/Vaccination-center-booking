from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class userprofile(models.Model):
    user=models.OneToOneField(User, related_name='userprofile',on_delete=models.CASCADE) #a user can only have one user profile - so onetoone
    
    def __str__(self) :
        return self.user.username
