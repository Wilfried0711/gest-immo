from customer.views import index , create,show, update, delete
from django.urls import path

urlpatterns = [
    path('', index, name="customer_home"),
    path('create/', create, name="create_customer" ),
    path('show/<int:id>',show, name="show_customer"),
    path('update/<int:id>',update, name="update_customer"),
    path('delete/<int:id>', delete, name="delete_customer")
    
]