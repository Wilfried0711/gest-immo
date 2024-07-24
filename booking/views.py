from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from booking.forms import BookingForm
from booking.models import Booking



# Create your views here.
def index (request):
    bookings = Booking.objects.all()
    context = {
        "bookings":bookings
    }
    
    return render(request,"booking/index.html",context)

def create(request):
    if request.method == "POST":

        form = BookingForm(request.POST)
        if form.is_valid():
            messages.success(request, "Résevation créée avec succes 😊")
            form.save()
            return redirect("booking_home")
        else:
            context = {
                "booking_form": form
            }
            return render(request, "booking/create.html", context)
        
    else:
        form = BookingForm()
        context= {
            "booking_form": form
        }
        
        return render(request, "booking/create.html", context)


def show(request,id):
    booking = Booking.objects.get(pk=id) 
    

    context = {
        'booking': booking
    }
    return render(request, "booking/show.html", context)

def update(request,id):
    booking_to_update = Booking.objects.get(pk=id)
    form =BookingForm(instance=booking_to_update)

    if request.method == "POST": 
        form =BookingForm(request.POST, instance=booking_to_update)
        if form.is_valid():
            form.save()
            messages.info(request, "Réservation modifiée avec succes")
            return redirect("booking_home")
        else:
            context = {
                "booking_form": form, 
                "booking_to_update": booking_to_update
            }
            return render(request, "booking/update.html", context)  
    else:
        context = {
            "booking_form": form, 
                "booking_to_update": booking_to_update
        }
        return render(request, "booking/update.html", context)
        
def delete(request, id):
    # Récupérer le client ou retourner une erreur 404 si le client n'existe pas
    booking = get_object_or_404(booking, pk=id)
    
    booking.delete()
    
    # Ajouter un message de confirmation
    messages.info(request, f"Réservation '{booking.id}' supprimée avec succès")
    
    return redirect("booking_home")
