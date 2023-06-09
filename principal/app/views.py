from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages, auth
from . import models



def app(request):
    return render(request,'home.html')

def login(request):    
    return render(request,'login.html')

def home(request):
    return render(request,'home.html')

def billetera(request):
    return render(request,'billetera.html')

def editar_medios_pagos(request):
    return render(request,'editar_medios_pagos.html')

def editar_saldo_usuario(request):
    return render(request,'editar_saldo_usuario.html')

def editar_tarifa_envio(request):
    return render(request,'editar_tarifa_envio.html')

def retirar_saldo(request):
    return render(request,'retirar_saldo.html')

def historial(request):
    return render(request,'historial.html')

def añadir_saldo(request):
    return render(request,'añadir_saldo.html')

def crear_cuenta(request):
    if request.method=='POST':

        nombres = request.POST['nombre']
        apellidos = request.POST['apellido']
        contraseña = request.POST['password']
        pais =request.POST['pais']
        ciudad =request.POST['ciudad']
        direccion = request.POST['direccion']
        tipo_documento = request.POST['tipocc']
        numero_documento = request.POST['cedula']
        fecha_expedicion_documento = request.POST['fechaexpedicion']
        correo_electronico = request.POST['email']
        celular = request.POST['numerocel']


        
        #cedula=request.POST['']
        #nombre=request.POST['nombre']

        Usuario=models.Usuario(   
            nombres=nombres,    
            apellidos=apellidos,
            contraseña=contraseña,
            pais=pais,
            ciudad=ciudad,
            direccion=direccion,
            tipo_documento=tipo_documento,
            numero_documento=numero_documento,
            fecha_expedicion_documento=fecha_expedicion_documento,
            correo_electronico=correo_electronico,
            celular=celular
        )

        Usuario.save()
    return render(request,'crear_cuenta.html')
# Create your views here.