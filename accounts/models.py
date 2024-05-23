from django.contrib.auth.models import AbstractUser 
from django.db import models 


# Custom user model
class CustomUser(AbstractUser):
    # add additional fields in here
    birthdate = models.DateField(null=True, blank=True)