from django.contrib import admin
from django.urls import path , include
from marriageapp import views

urlpatterns = [
    path('' , views.index , name='index'),
    path('signin' , views.signin , name='signin'),
    path('signup' , views.signup , name='signup'),
    path('contact' , views.contact , name='contact'),
    path('booking' , views.booking , name='booking'),
    path('booked-bookings' , views.bBooking , name='bookedbooking'),   
    path('logoutUser' , views.logoutUser , name='logoutUser'),
    path('search' , views.search , name='search'),
    path('delete/<int:serial_number>' , views.delete , name='delete'),
    path('edit/<int:serial_number>' , views.edit , name='edit'),
    path('edit/editrecord/<int:serial_number>' , views.editrecord , name='editrecord'),
    path('slip/<int:serial_number>' , views.slip , name='slip'),
]
