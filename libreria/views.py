from django.shortcuts import render, redirect, get_object_or_404
from .models import Auto, Usuario, Empleado
from .forms import AutoForm,  UsuarioForm, EmpleadoForm
from django import views
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages


# Create your views here.

def is_superuser(user):
    return user.is_superuser


def inicio(request):
    return render(request, 'paginas/inicio.html')

@login_required
@user_passes_test(is_superuser)
def usuarios(request):  
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/usuarios.html', {'usuarios': usuarios})

@login_required
@user_passes_test(is_superuser)
def empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleados/empleados.html', {'empleados': empleados})

@login_required
@user_passes_test(is_superuser)
def autos(request):
    autos = Auto.objects.all()
    return render(request, 'autos/index.html', {'autos': autos})

def vehiculos(request):
    return render(request, 'paginas/vehiculos.html')

def locales(request):
    return render(request, 'paginas/locales.html')

def contacto(request):
    return render(request, 'paginas/contacto.html')


#CRUD AUTO
@login_required
@user_passes_test(is_superuser)
def crear_auto(request):
    #Request FILE recepciona archivos
    formulario = AutoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid(): #Recepcionar datos
        formulario.save() #Guardar datos
        return redirect('autos') #Redireccionar datos
    return render(request, 'autos/crear.html', {'formulario': formulario})
@login_required
@user_passes_test(is_superuser)
def editar_auto(request, id):
    auto = Auto.objects.get(id=id)
    formulario = AutoForm(request.POST or None, request.FILES or None, instance=auto)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('autos')
        
    return render(request, 'autos/editar.html', {'formulario': formulario})
@login_required
@user_passes_test(is_superuser)
def eliminar_auto(request, id):
    auto = get_object_or_404(Auto, id=id)
    auto.delete()
    messages.success(request, 'Auto eliminado correctamente')
    return redirect('autos')


#CRUD USUARIO
@login_required
@user_passes_test(is_superuser)
def crear_usuario(request):
    #Request FILE recepciona archivos
    formulario_usuario = UsuarioForm(request.POST or None, request.FILES or None)
    if formulario_usuario.is_valid(): #Recepcionar datos
        formulario_usuario.save() #Guardar datos
        return redirect('usuarios') #Redireccionar datos
    return render(request, 'usuarios/crear_usuario.html', {'formulario': formulario_usuario})
@login_required
@user_passes_test(is_superuser)    
def editar_usuario(request, id):
    usuario = Usuario.objects.get(id=id)
    formulario_usuario = UsuarioForm(request.POST or None, request.FILES or None, instance=usuario)
    if formulario_usuario.is_valid() and request.POST:
        formulario_usuario.save()
        return redirect('usuarios')
        
    return render(request, 'usuarios/editar_usuario.html', {'formulario': formulario_usuario})
@login_required
@user_passes_test(is_superuser)
def eliminar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    usuario.delete()
    messages.success(request, 'Usuario eliminado correctamente')
    return redirect('usuarios')

#CRUD EMPLEADO
@login_required
@user_passes_test(is_superuser)
def crear_empleado(request):
    #Request FILE recepciona archivos
    formulario_empleado = EmpleadoForm(request.POST or None, request.FILES or None)
    if formulario_empleado.is_valid(): #Recepcionar datos
        formulario_empleado.save() #Guardar datos
        return redirect('empleados') #Redireccionar datos
    return render(request, 'empleados/crear_empleado.html', {'formulario': formulario_empleado})
@login_required
@user_passes_test(is_superuser)   
def editar_empleado(request, id):
    empleado = Empleado.objects.get(id=id)
    formulario_empleado = EmpleadoForm(request.POST or None, request.FILES or None, instance=empleado)
    if formulario_empleado.is_valid() and request.POST:
        formulario_empleado.save()
        return redirect('empleados')
        
    return render(request, 'empleados/editar_empleado.html', {'formulario': formulario_empleado})
@login_required
@user_passes_test(is_superuser)
def eliminar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    empleado.delete()
    messages.success(request, 'Empleado eliminado correctamente')
    return redirect('empleados')


#REGISTRO

def registrar(request):
    if request.method == 'GET':
        return render(request, 'registration/registro.html', {'form': UserCreationForm()})
    else: 
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('inicio')
            except IntegrityError:
                return render(request, 'registration/registro.html', {'form': UserCreationForm(), 'error': 'El usuario ya existe'})
        return render(request, 'registration/registro.html', {'form': UserCreationForm(), 'error': 'Las contraseñas no coinciden'})
        

def iniciar_sesion(request):
    if request.method == 'GET':
        return render(request, 'registration/iniciar_sesion.html', {'form': AuthenticationForm()})
    else: 
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'registration/iniciar_sesion.html', {'form': AuthenticationForm(), 'error': 'Usuario y/o contraseña incorrectos'})
        else:
            login(request, user)
            return redirect('inicio')
   


def cerrar_sesion(request):
    logout(request)
    return redirect('inicio')