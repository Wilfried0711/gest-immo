from owner.views import index , create,show, update, delete
from django.urls import path

urlpatterns = [
    path('', index, name="owner_home"),
    path('create/', create, name="create_owner" ),
    path('show/<int:id>',show, name="show_owner"),
    path('update/<int:id>',update, name="update_owner"),
    path('delete/<int:id>', delete, name="delete_owner")
    
]