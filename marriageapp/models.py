from django.db import models
# Create your models here.
class Responses(models.Model):
    username = models.CharField(max_length=15)
    message = models.CharField(max_length = 40)
    date = models.DateField()


class Bookingss(models.Model):
    serial_number = models.IntegerField(null = True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    cnic = models.CharField(max_length=50)
    events = models.CharField(max_length=50)
    amount = models.CharField(max_length= 50)
    date = models.DateField()
    def __str__(self):
          return f"{self.fname} {self.lname} {self.cnic}"

