from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User 
from django.contrib.auth import login , logout , authenticate
from datetime import datetime
from marriageapp.models import Responses , Bookingss
from django.db.models import Max
# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect('/signin')
    return render(request , 'index.html')


def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        rpassword = request.POST.get("rpassword")
        print(username, password)
        if password == rpassword:
            user = User.objects.create_user(username, email , password)
            user.save()
            return redirect('/signin')
    return render(request, 'signup.html')

def signin(request):
    if request.method == "POST":
      username =request.POST.get("username")
      password = request.POST.get("password")
      print(username, password)
      user = authenticate(request, username=username , password=password)
      if user is not None:
          login(request, user)
          return redirect('/')
      else:
           print("Some error occured")
           return render(request, 'signin.html')
    return render(request , 'signin.html')
def contact(request):
    if request.user.is_anonymous:
        return redirect('/signin')
    if request.method == "POST":
        username = request.POST.get("username")
        message = request.POST.get("message")
        responses = Responses(username=username , message=message, date= datetime.today())
        responses.save()

        

    return render(request, 'contact.html')
    # return HttpResponse("This is a about page")

def booking(request):
    if request.user.is_anonymous:
        return redirect('/signin')
    serial_number = 1 if Bookingss.objects.count()==0 else Bookingss.objects.aggregate(max = Max('serial_number'))["max"]+1
    if request.method == "POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        cnic = request.POST.get("cnic")
        events = request.POST.get("events")
        amount = request.POST.get("amount")
        date = request.POST.get("date")
        bookingss = Bookingss(serial_number= serial_number, fname=fname , lname=lname, cnic=cnic, events=events, amount=amount , date=date  )
        print(bookingss)
        bookingss.save()
        return redirect('/booking')
    return render(request, 'booking.html' , locals())
    # return HttpResponse("This is a about page")




def bBooking(request):
    if request.user.is_anonymous:
        return redirect('/signin')
    data = Bookingss.objects.order_by('serial_number')
    print(data)
    return render(request, 'bookedbooking.html', {'data': data})
    # return HttpResponse("This is a about page")



def delete(request , serial_number):
     member = Bookingss.objects.get(serial_number=serial_number)
     member.delete()
     return redirect('/booked-bookings') 


def logoutUser(request):
    logout(request)
    return redirect('/signin')

def edit(request , serial_number):
    edits = Bookingss.objects.get(serial_number = serial_number)
    return render(request, "edit.html" , {'edits': edits})

def editrecord(request , serial_number):
    fname = request.POST.get("fname")
    lname = request.POST.get("lname")
    cnic = request.POST.get("cnic")
    events = request.POST.get("events")
    amount = request.POST.get("amount")
    date = request.POST.get("date")
    update = Bookingss.objects.get(serial_number=serial_number)
    update.fname = fname
    update.lname = lname
    update.cnic = cnic
    update.events = events
    update.amount = amount
    update.date = date
    update.save()
    return redirect('/booked-bookings')

def search(request):
  if request.method == "GET":
        search_query = request.GET.get("search")
        if search_query:
            alldata = Bookingss.objects.filter(serial_number__contains=search_query) 
            return render(request, 'search.html', {'alldata': alldata})
        else:
            return render(request, 'search.html', {})
        



def slip(request, serial_number):
    data = Bookingss.objects.get(serial_number=serial_number)
    return render(request, 'slip.html', {'data': data})
        