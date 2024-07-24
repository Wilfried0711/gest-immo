from django.db import models
from owner.models import Owner

# Create your models here.
class Poperty(models.Model):
    
    VILLA = 'villa'
    APPARTEMENT = 'appartement'
    STORE = 'store'
    
    PROPERTY_TYPE_CHOICES = [
        (VILLA, 'Villa'),
        (APPARTEMENT, 'Appartement'),
        (STORE, 'Store'),
    ]
    
    name = models.CharField(max_length= 5000)
    description = models.TextField(max_length= 55000)
    price = models.PositiveIntegerField(null=True, blank=True)
    superficy = models.PositiveIntegerField(null=True, blank=True)
    type = models.CharField(max_length=20,choices=PROPERTY_TYPE_CHOICES, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to="poperty/", default="default.jpg")
    bedrooms = models.PositiveSmallIntegerField(null=True, blank=True)
    bathrooms = models.PositiveIntegerField(null=True, blank=True)
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True,null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True,null=True, blank=True)

    
    def __str__(self):
        return self.name