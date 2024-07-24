from booking.views import index , create,show, update, delete
from django.urls import path

urlpatterns = [
    path('', index, name="booking_home"),
    path('create/', create, name="create_booking" ),
    path('show/<int:id>',show, name="show_booking"),
    path('update/<int:id>',update, name="update_booking"),
    path('delete/<int:id>', delete, name="delete_booking")
    
]