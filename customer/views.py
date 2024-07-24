from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.contrib import messages
from customer.forms import CustomerForm
from customer.models import Customer



# Create your views here.
def index (request):
    customers = Customer.objects.all()
    context = {
        "customers":customers
    }
    
    return render(request,"customers/index.html",context)

def create(request):
    if request.method == "POST":

        form = CustomerForm(request.POST)
        if form.is_valid():
            messages.success(request, "Client créé avec 😊")
            form.save()
            return redirect("customer_home")
        else:
            context = {
                "customer_form": form
            }
            return render(request, "customers/create.html", context)
        
    else:
        form = CustomerForm()
        context= {
            "customer_form": form
        }
        
        return render(request, "customers/create.html", context)


def show(request,id):
    customer = Customer.objects.get(pk=id) 
    

    context = {
        'customer': customer
    }
    return render(request, "customers/show.html", context)

def update(request,id):
    customer_to_update = Customer.objects.get(pk=id)
    form =CustomerForm(instance=customer_to_update)

    if request.method == "POST": 
        form =CustomerForm(request.POST, instance=customer_to_update)
        if form.is_valid():
            form.save()
            messages.info(request, "Client modifie avec succes")
            return redirect("customer_home")
        else:
            context = {
                "customer_form": form, 
                "customer_to_update": customer_to_update
            }
            return render(request, "customers/update.html", context)  
    else:
        context = {
            "customer_form": form, 
                "customer_to_update": customer_to_update
        }
        return render(request, "customers/update.html", context)
        
def delete(request, id):
    # Récupérer le client ou retourner une erreur 404 si le client n'existe pas
    customer = get_object_or_404(Customer, pk=id)
    
    customer.delete()
    
    # Ajouter un message de confirmation
    messages.info(request, f"Client '{customer.lastname} {customer.firstname}' supprimé avec succès")
    
    # Rediriger vers la page d'accueil des clients
    return redirect("customer_home")