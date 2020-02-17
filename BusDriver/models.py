from django.db import models
from django.urls import reverse


class Driver(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100,blank=True,null=True)
    phone = models.CharField(max_length=12,null=True,blank=True)
    age = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.name


class Bus(models.Model):
    origin = models.CharField(max_length=20)
    destination = models.CharField(max_length=20)
    SeatsNumber = models.IntegerField()
    PreservedSeats = models.IntegerField(default=0,editable=False)
    isFull = models.BooleanField(default=False,editable=False,blank=True,null=True)
    DepartureTime = models.DateTimeField(null=True,blank=True)
    drivername = models.ForeignKey(Driver,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.destination
