from poperty.views import index , create,show, update, delete
from django.urls import path

urlpatterns = [
    path('', index, name="poperty_home"),
    path('create/', create, name="create_poperty" ),
    path('show/<int:id>',show, name="show_poperty"),
    path('update/<int:id>',update, name="update_poperty"),
    path('delete/<int:id>', delete, name="delete_poperty")
    
]