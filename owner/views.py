from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.contrib import messages
from owner.forms import OwnerForm
from owner.models import Owner



# Create your views here.
def index (request):
    owners = Owner.objects.all()
    context = {
        "owners":owners
    }
    
    return render(request,"owners/index.html",context)

def create(request):
    if request.method == "POST":

        form = OwnerForm(request.POST)
        if form.is_valid():
            messages.success(request, "Propriétaire créé avec 😊")
            form.save()
            return redirect("owner_home")
        else:
            context = {
                "owner_form": form
            }
            return render(request, "owners/create.html", context)
        
    else:
        form = OwnerForm()
        context= {
            "owner_form": form
        }
        
        return render(request, "owners/create.html", context)


def show(request,id):
    owner = Owner.objects.get(pk=id) 
    

    context = {
        'owner': owner
    }
    return render(request, "owners/show.html", context)

def update(request,id):
    owner_to_update = get_object_or_404(Owner, pk=id)

    if request.method == "POST": 
        form = OwnerForm(request.POST, instance=owner_to_update)
        if form.is_valid():
            form.save()
            messages.info(request, "Propriétaire modifié avec succes")
            return redirect("owner_home")
        else:
            context = {
                "owner_form": form, 
                    "owner_to_update": owner_to_update
            }
            return render(request, "owners/update.html", context)  
    else:
        form = OwnerForm(instance=owner_to_update)
        
        context = {
            "owner_form": form,
            "owner_to_update": owner_to_update
        }
        return render(request, "owners/update.html", context)
        
def delete(request, id):
    # Récupérer le Propriétaire ou retourner une erreur 404 si le Propriétaire n'existe pas
    owner = get_object_or_404(Owner, pk=id)
    
    owner.delete()
    
    # Ajouter un message de confirmation
    messages.info(request, f"Propriétaire '{owner.lastname} {owner.firstname}' supprimé avec succès")
    
    # Rediriger vers la page d'accueil des Propriétaires
    return redirect("owner_home")