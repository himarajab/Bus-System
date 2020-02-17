from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .forms import BusForm,DriverForm
from .filters import BusFilter


def home(request):
    buses = Bus.objects.all()
    drivers = Driver.objects.all()
    myFilter = BusFilter(request.GET ,queryset=buses)
    buses = myFilter.qs
    context = {'buses':buses,'drivers':drivers,'myFilter':myFilter}
    return render(request, 'BusDriver/dashboard.html', context)


def driver(request,pk):
    driver = Driver.objects.get(id = pk)
    context = {
        'driver':driver
    }
    return render(request,'BusDriver/Driver.html',context)


def create_driver(request):
    form = DriverForm()
    if request.method == 'POST':
        form = DriverForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'BusDriver/driver_form.html', context)


def update_driver(request, pk):
    driver = Driver.objects.get(id=pk)
    form = DriverForm(instance=driver)

    if request.method == 'POST':
        form = DriverForm(request.POST, instance=driver)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'BusDriver/driver_form.html', context)


def delete_driver(request, pk):
    driver = Driver.objects.get(id=pk)
    if request.method == "POST":
        driver.delete()
        return redirect('/')

    context = {'driver': driver}
    return render(request, 'BusDriver/delete.html', context)

def bus(request,pk):
    bus = Bus.objects.get(id = pk)

    context = {
        'bus':bus
    }
    return render(request,'BusDriver/Bus.html',context)


def create_bus(request):
    form = BusForm()
    if request.method == 'POST':
        form = BusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'BusDriver/bus_form.html', context)


def update_bus(request, pk):
    bus = Bus.objects.get(id=pk)
    form = BusForm(instance=bus)

    if request.method == 'POST':
        form = BusForm(request.POST, instance=bus)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'BusDriver/bus_form.html', context)


def delete_bus(request, pk):
    bus = Bus.objects.get(id=pk)
    if request.method == "POST":
        bus.delete()
        return redirect('/')

    context = {'bus': bus}
    return render(request, 'BusDriver/delete_bus.html', context)
