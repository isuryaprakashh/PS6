from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class TenentUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def _str_(self):
        return self.username

# tenentapp/models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class TenentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='tenent_profile_images/',blank=True,null=True,help_text="Upload a profile picture (Optional)")
    email = models.EmailField(max_length=255,null=True,blank=True,help_text="Your email address")
    phone_number = models.CharField(max_length=15,blank=True,null=True,help_text="Enter your contact number")
    address = models.TextField(blank=True,null=True,help_text="Your complete address")
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Set email from user's email if not provided
        if not self.email:
            self.email = self.user.email
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username}'s Profile"

    class Meta:
        verbose_name = "Tenant Profile"
        verbose_name_plural = "Tenant Profiles"

