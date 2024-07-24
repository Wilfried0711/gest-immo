from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['customer_id','poperty_id','StartDate','EndDate','StartTime','EndTime','amount','status']