from hashlib import pbkdf2_hmac
from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.

class Client(models.Model):
    client_name = models.CharField(max_length=100, null=True, blank=True)
    company_name = models.CharField(max_length=100, null=True, blank=True)
    client_mobile_number = models.CharField(max_length=20, null=True, blank=True)
    client_email = models.CharField(unique=True, null=False, blank=False)
    password = models.CharField(max_length=128)

    def save(self, *args, **kwargs):
        if not self.password.startswith('pbkdf2_'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)