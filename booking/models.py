from django.db import models
from customer.models import Customer
from poperty.models import Poperty

# Create your models here.
class Booking(models.Model):
    
    PENDING = 'pending'
    PAID = 'paid'
    CANCELLED = 'cancelled'
    
    BOOKING_TYPE_CHOICES = [
        (PENDING, 'pending'),
        (PAID, 'paid'),
        (CANCELLED, 'cancelled'),
    ]
    
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    poperty_id = models.ForeignKey(Poperty, on_delete=models.CASCADE, null=True, blank=True)
    StartDate = models.DateTimeField(null=True, blank=True)
    EndDate = models.DateTimeField(null=True, blank=True)
    StartTime = models.TimeField()
    EndTime = models.TimeField()
    amount = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=BOOKING_TYPE_CHOICES)

    
    