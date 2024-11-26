from django.shortcuts import render, redirect
from .models import Clientes
# Create your views here.

def inicio_vistaClientes(request):
    losclientes=Clientes.objects.all

    return render(request,"gestionarClientes.html", {"misclientes":losclientes})

def registrarClientes(request):
    id_cliente=request.POST["txtcliente"]
    nombre=request.POST["txtnombre"]
    telefono=request.POST["telefono"]
    correo=request.POST["txtcorreo"]
    fecha_n=request.POST["txtfecha"]
    historial_c=request.POST["txthistorial_c"]
    domicilio=request.POST["txtdomicilio"]
    guardarcliente=Clientes.objects.create(id_cliente=id_cliente, nombre=nombre, telefono=telefono, correo=correo, fecha_n=fecha_n, historial_c=historial_c, domicilio=domicilio)
    return redirect("clientes")

def seleccionarClientes(request,id_cliente):
    cliente=Clientes.objects.get(id_cliente=id_cliente)
    return render(request, "editarCliente.html", {"misclientes": cliente})

def editarClientes(request):
    id_cliente=request.POST["txtcliente"]
    nombre=request.POST["txtnombre"]
    telefono=request.POST["telefono"]
    correo=request.POST["txtcorreo"]
    fecha_n=request.POST["txtfecha"]
    historial_c=request.POST["txthistorial_c"]
    domicilio=request.POST["txtdomicilio"]
    cliente=Clientes.objects.get(id_cliente=id_cliente)
    cliente.id_cliente=id_cliente
    cliente.nombre=nombre
    cliente.telefono=telefono
    cliente.correo=correo
    cliente.fecha_n=fecha_n
    cliente.historial_c=historial_c
    cliente.domicilio=domicilio
    cliente.save()
    return redirect("clientes")

def borrarClientes(request, id_cliente):
    cliente=Clientes.objects.get(id_cliente=id_cliente)
    cliente.delete()

    return redirect("clientes")