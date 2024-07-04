from django.shortcuts import render
from booking.models import Plumber
from django.http import JsonResponse
# Create your views here.
def index(request):
    return render(request,'index.html')

def bookings(request):
    
    return render(request,"booking.html")

def submit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        location = request.POST.get('location')
        service = request.POST.get('service')
        abc= Plumber(Name=name,Phone=phone,Location=location,Service=service,)
        abc.save()
    return render(request,"submit.html")

def view_booking(request):
     return render(request,"view_booking.html")

 

def get_details(requst):
    books=list(Plumber.objects.values())
    return JsonResponse(books,safe=False)
