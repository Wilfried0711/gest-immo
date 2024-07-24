from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from poperty.forms import PopertyForm
from poperty.models import Poperty



# Create your views here.
def index (request):
    poperties = Poperty.objects.all()
    context = {
        "poperties":poperties
    }
    
    return render(request,"poperties/index.html",context)

def create(request):
    if request.method == "POST":

        form = PopertyForm(request.POST)
        if form.is_valid():
            messages.success(request, "Client créé avec 😊")
            form.save()
            return redirect("poperty_home")
        else:
            context = {
                "poperty_form": form
            }
            return render(request, "poperties/create.html", context)
        
    else:
        form = PopertyForm()
        context= {
            "poperty_form": form
        }
        
        return render(request, "poperties/create.html", context)


def show(request,id):
    poperty = Poperty.objects.get(pk=id) 
    

    context = {
        'poperty': poperty
    }
    return render(request, "poperties/show.html", context)

def update(request,id):
    poperty_to_update = Poperty.objects.get(pk=id)
    form =PopertyForm(instance=poperty_to_update)

    if request.method == "POST": 
        form =PopertyForm(request.POST, instance=poperty_to_update)
        if form.is_valid():
            form.save()
            messages.info(request, "Propriété modifiée avec succes")
            return redirect("poperty_home")
        else:
            context = {
                "poperty_form": form, 
                "poperty_to_update": poperty_to_update
            }
            return render(request, "Poperties/update.html", context)  
    else:
        context = {
            "poperty_form": form, 
                "poperty_to_update": poperty_to_update
        }
        return render(request, "poperties/update.html", context)
        
def delete(request, id):
    # Récupérer le client ou retourner une erreur 404 si le client n'existe pas
    poperty = get_object_or_404(Poperty, pk=id)
    
    poperty.delete()
    
    # Ajouter un message de confirmation
    messages.info(request, f"Client '{poperty.lastname} {poperty.firstname}' supprimé avec succès")
    
    return redirect("poperty_home")
