from django.shortcuts import render, redirect
from .models import Vehiculo
# Create your views here.

def inicio_vistaVehiculo(request):
    elcarro=Vehiculo.objects.all

    return render(request,"gestionarVehiculo.html", {"micarro":elcarro})

def registrarVehiculo(request):
    id_vehiculo=request.POST["txtcodigo_v"]
    marca=request.POST["txtmarca"]
    modelo=request.POST["txtmodelo"]
    año=request.POST["txtaño"]
    estado=request.POST["txtestado_v"]
    kilometraje=request.POST["txtkilometraje"]
    guardarvehiculo=Vehiculo.objects.create(id_vehiculo=id_vehiculo, marca=marca, modelo=modelo, año=año, estado=estado, kilometraje=kilometraje)
    return redirect("vehiculo")

def seleccionarVehiculo(request,id_vehiculo):
    vehiculo=Vehiculo.objects.get(id_vehiculo=id_vehiculo)
    return render(request, "editarVehiculo.html", {"micarro": vehiculo})

def editarVehiculo(request):
    id_vehiculo=request.POST["txtcodigo_v"]
    marca=request.POST["txtmarca"]
    modelo=request.POST["txtmodelo"]
    año=request.POST["txtaño"]
    estado=request.POST["txtestado_v"]
    kilometraje=request.POST["txtkilometraje"]
    vehiculo=Vehiculo.objects.get(id_vehiculo=id_vehiculo)
    vehiculo.id_vehiculo=id_vehiculo
    vehiculo.marca=marca
    vehiculo.modelo=modelo
    vehiculo.año=año
    vehiculo.estado=estado
    vehiculo.kilometraje=kilometraje
    vehiculo.save()
    return redirect("vehiculo")

def borrarVehiculo(request, id_vehiculo):
    vehiculo=Vehiculo.objects.get(id_vehiculo=id_vehiculo)
    vehiculo.delete()

    return redirect("vehiculo")