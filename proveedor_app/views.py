from django.shortcuts import render, redirect
from .models import Proveedor
# Create your views here.

def inicio_vistaProveedor(request):
    losproveedores=Proveedor.objects.all

    return render(request,"gestionarProveedores.html", {"misproveedores":losproveedores})

def registrarProveedor(request):
    id_proveedor=request.POST["txtproveedor"]
    nombre=request.POST["txtnombre"]
    direccion=request.POST["txtdireccion"]
    telefono=request.POST["txttelefono"]
    representante=request.POST["txtrepresentante"]
    tipo_pago=request.POST["txttipo_pago"]
    guardarproveedor=Proveedor.objects.create(id_proveedor=id_proveedor, nombre=nombre, direccion=direccion, telefono=telefono, representante=representante, tipo_pago=tipo_pago)
    return redirect("proveedor")

def seleccionarProveedor(request,id_proveedor):
    proveedor=Proveedor.objects.get(id_proveedor=id_proveedor)
    return render(request, "editarProveedor.html", {"misproveedores": proveedor})

def editarProveedor(request):
    id_proveedor=request.POST["txtproveedor"]
    nombre=request.POST["txtnombre"]
    direccion=request.POST["txtdireccion"]
    telefono=request.POST["txttelefono"]
    representante=request.POST["txtrepresentante"]
    tipo_pago=request.POST["txttipo_pago"]
    proveedor=Proveedor.objects.get(id_proveedor=id_proveedor)
    proveedor.id_proveedor=id_proveedor
    proveedor.nombre=nombre
    proveedor.direccion=direccion
    proveedor.telefono=telefono
    proveedor.representante=representante
    proveedor.tipo_pago=tipo_pago
    proveedor.save()
    return redirect("proveedor")

def borrarProveedor(request, id_proveedor):
    proveedor=Proveedor.objects.get(id_proveedor=id_proveedor)
    proveedor.delete()

    return redirect("proveedor")