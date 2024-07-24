from django.db import models

# Create your models here.
class Owner(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=500)
    phone = models.CharField(max_length=13)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length= 5000)
    
    
    def __str__(self):
        return self.lastname