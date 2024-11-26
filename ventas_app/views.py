from django.shortcuts import render, redirect
from .models import Ventas
# Create your views here.

def inicio_vistaVentas(request):
    laventa=Ventas.objects.all

    return render(request,"gestionarVentas.html", {"miventa":laventa})

def registrarVenta(request):
    id_venta=request.POST["txtventa_c"]
    fecha=request.POST["txtfecha"]
    cliente_a=request.POST["txtcliente_a"]
    vehiculo_v=request.POST["txtvehiculo_v"]
    precio_f=request.POST["txtprecio_f"]
    metodo_p=request.POST["txtmetodo_p"]
    guardarventa=Ventas.objects.create(id_venta=id_venta, fecha=fecha, cliente_a=cliente_a, vehiculo_v=vehiculo_v, precio_f=precio_f, metodo_p=metodo_p)
    return redirect("venta")

def seleccionarVenta(request,id_venta):
    venta=Ventas.objects.get(id_venta=id_venta)
    return render(request, "editarVenta.html", {"miventa": venta})

def editarVenta(request):
    id_venta=request.POST["txtventa_c"]
    fecha=request.POST["txtfecha"]
    cliente_a=request.POST["txtcliente_a"]
    vehiculo_v=request.POST["txtvehiculo_v"]
    precio_f=request.POST["txtprecio_f"]
    metodo_p=request.POST["txtmetodo_p"]
    venta=Ventas.objects.get(id_venta=id_venta)
    venta.id_venta=id_venta
    venta.fecha=fecha
    venta.cliente_a=cliente_a
    venta.vehiculo_v=vehiculo_v
    venta.precio_f=precio_f
    venta.metodo_p=metodo_p
    venta.save()
    return redirect("venta")

def borrarVenta(request, id_venta):
    venta=Ventas.objects.get(id_venta=id_venta)
    venta.delete()

    return redirect("venta")