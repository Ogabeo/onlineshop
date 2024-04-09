from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone =models.CharField(max_length=20, null=True, blank=True)
    photos=models.ImageField(upload_to='users/', default='default/i.webp', blank=True)
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.username
    

    