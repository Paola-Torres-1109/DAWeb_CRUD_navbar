from django.shortcuts import render, redirect
from .models import Empleados
# Create your views here.

def inicio_vistaEmpleados(request):
    losempleados=Empleados.objects.all

    return render(request,"gestionarEmpleados.html", {"misempleados":losempleados})

def registrarEmpleado(request):
    id_empleado=request.POST["txtempleado"]
    nombre=request.POST["txtnombre"]
    cargo=request.POST["txtcargo"]
    salario=request.POST["txtsalario"]
    turno=request.POST["txtturno"]
    departamento=request.POST["txtdepartamento"]
    guardarempleado=Empleados.objects.create(id_empleado=id_empleado, nombre=nombre, cargo=cargo, salario=salario, turno=turno, departamento=departamento)
    return redirect("empleado")

def seleccionarEmpleado(request,id_empleado):
    empleado=Empleados.objects.get(id_empleado=id_empleado)
    return render(request, "editarEmpleado.html", {"misempleados": empleado})

def editarEmpleado(request):
    id_empleado=request.POST["txtempleado"]
    nombre=request.POST["txtnombre"]
    cargo=request.POST["txtcargo"]
    salario=request.POST["txtsalario"]
    turno=request.POST["txtturno"]
    departamento=request.POST["txtdepartamento"]
    empleado=Empleados.objects.get(id_empleado=id_empleado)
    empleado.id_empleado=id_empleado
    empleado.nombre=nombre
    empleado.cargo=cargo
    empleado.salario=salario
    empleado.turno=turno
    empleado.departamento=departamento
    empleado.save()
    return redirect("empleado")

def borrarEmpleado(request, id_empleado):
    empleado=Empleados.objects.get(id_empleado=id_empleado)
    empleado.delete()

    return redirect("empleado")