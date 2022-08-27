from django.shortcuts import render
from .models import dimsumItems, appetizerItems, baoItems, noodleSoupItems, sushiItems, dessertItems, drinkItems, reservations, notification
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from twilio.rest import Client

# Create your views here.
def home(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'about/index.html', {'title': 'About'})

def menu(request):
    menuItems = {'dimsum_items': dimsumItems.objects.all(),
                'appetizer_items': appetizerItems.objects.all(),
                'noodleSoup_items': noodleSoupItems.objects.all(),
                'bao_items': baoItems.objects.all(),
                'sushi_items': sushiItems.objects.all(),
                'dessert_items': dessertItems.objects.all(),
                'drink_items': drinkItems.objects.all(),
    }
    return render(request, 'menu/index.html', menuItems)

def reservationsPage(request, methods = ["GET", "POST"]):
    if request.method == 'POST':
        if request.POST.get('date') and request.POST.get('time') and request.POST.get('people') and request.POST.get('name') and request.POST.get('phone') and request.POST.get('email'):

            reservation = reservations()
            reservation.date = request.POST.get('date')
            reservation.time = request.POST.get('time')
            reservation.people = request.POST.get('people')
            reservation.title = request.POST.get('name')
            reservation.phone = request.POST.get('phone')
            reservation.email = request.POST.get('email')
            reservation.save()

            messages.success(request, f"Thank you, {reservation.title}, your reservation has successfully been booked.")

            subject = f'Densetsu: Reservation Confirmation for {reservation.title} on {reservation.date}.'
            message = f'Hello {reservation.title}, you have successfully booked a reservation on {reservation.date} at {reservation.time}. Please contact (760) 309-3706 to cancel or change your reservation.'
            send_mail(subject, message, settings.EMAIL_HOST_USER, [reservation.email])

            message_to_text = (f"Hi {reservation.title}, you've scheduled a reservation at Densetsu NYC on {reservation.date} at {reservation.time}. To change or cancel your reservation, please call (760) 309-3706. In the mean time, check out our website at densetsunyc.com! We can't wait to see you!")

            number = reservation.phone
            number_cleaned = number.replace('-' and '(' and ')' and ' ','')
            number_final = "+1" + number_cleaned

            client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
            client.messages.create(to = number_final, from_=settings.TWILIO_NUMBER, body=message_to_text)

            return render(request, 'reservations/index.html')
        else:
            messages.error(request, f"Something went wrong. Please make sure to complete all fields below and try again!")
            return render(request, 'reservations/index.html')
    return render(request, 'reservations/index.html')

def gallery(request):
    return render(request, 'gallery/index.html')

def contact(request, methods = ["GET", "POST"]):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('email') and request.POST.get('phone') and request.POST.get('message'):
            contact = notification()
            contact.title = request.POST.get('name')
            contact.email = request.POST.get('email')
            contact.phone = request.POST.get('phone')
            contact.message = request.POST.get('message')
            contact.save()

            messages.success(request, "Thank you. Your request has been submitted!")
            return render(request, 'contact/index.html')
        else:
            messages.error(request, "Something went wrong. Please make sure to complete all fields below and try again!")
            return render(request, 'contact/index.html')
    return render(request, 'contact/index.html')

def copyright(request):
    return render(request, 'copyright/index.html')
