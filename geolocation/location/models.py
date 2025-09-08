from django.contrib.auth.models import AbstractUser
from django.db import models



# Create your models here.

class User(AbstractUser):
    pass

class Location(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='location')
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Location"
