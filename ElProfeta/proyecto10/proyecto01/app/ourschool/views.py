
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render, redirect
from .models import Usuario
from .models import *

def inicio(request):
    return render(request, 'ourschool/inicio.html')


def inicio_estudiante(request):
    return render(request, 'ourschool/inicio_estudiante.html')


def iniciar(request):
    email = None
    clave = None

    if request.method == "POST":
        email = request.POST.get("correo")
        clave = request.POST.get("contrasena")

    try:
        usuario = Usuario.objects.get(correo=email, contrasena=clave)
        messages.success(request, "Bienvenido!")

        request.session['logueo'] = {'rol': usuario.rol,'correo':usuario.correo}
        if usuario.rol == 2:
            return render(request, 'ourschool/inicio_estudiante.html')
        elif usuario.rol == 3:
            return render(request, 'ourschool/inicio_estudiante.html')
        elif usuario.rol == 1:
            return redirect('lista_usuarios')
        else:
            messages.error(request, "Rol no válido")

    except Usuario.DoesNotExist:
        messages.error(request, "Usuario o contraseña no válidos")
        return render(request, 'ourschool/iniciar.html')


def cerrar_session(request):
    try:
        del request.session['logueo']
        messages.success(request, 'Sesión cerrada correctamente')
        return redirect('inicio')

    except Exception as e:
        messages.error(request, f'Error: {e}')
        return redirect('inicio') 


def registro(request):
    if request.method == "POST":
        
        nom_ape = request.POST.get('nombre_apellido')
        tipo_doc = request.POST.get('tipo_documento')
        num_doc = request.POST.get('numero_documento')
        tel = request.POST.get('telefono')
        cor = request.POST.get('correo')
        fec_nac = request.POST.get('fecha_nacimiento')
        contr = request.POST.get('contrasena')
        r = request.POST.get('rol')

        try:
            
            nuevo_usuario = Usuario(
                nombre_apellido=nom_ape,
                tipo_documento=tipo_doc,
                numero_documento=num_doc,
                telefono=tel,
                correo=cor,
                fecha_nacimiento=fec_nac,
                contrasena=contr,
                rol=r
            )
            
            nuevo_usuario.full_clean()
            nuevo_usuario.save()
            messages.success(request, 'Se guardó correctamente')
            return redirect('iniciar')
        except ValidationError as e:
            messages.warning(request, f'Error: {e}')

    return HttpResponseRedirect(reverse('inicio'))


def lista_usuarios(request):
    data = Usuario.objects.all()
    return render(request, 'ourschool/inicio_estudiante.html', {'data': data})


def guardar(request):
    if request.method == "POST":
        id = request.POST.get("id")
        nomb = request.POST.get("nombre")
        desc = request.POST.get("descripcion")

        if id == "":
            
            try:
                cat = Categoria(
                    nombre=nomb,
                    descripcion=desc
                )
                cat.save()
                messages.success(request, "Guardado correctamente!!")
            except Exception as e:
                messages.error(request, f"Error. {e}")
        else:
            
            try:
                q = Categoria.objects.get(pk=id)
                q.nombre = nomb
                q.descripcion = desc
                q.save()
                messages.success(request, "Actualizado correctamente!!")
            except Exception as e:
                messages.error(request, f"Error. {e}")

        return HttpResponseRedirect(reverse("tienda:listar_categorias", args=()))
    else:
        messages.warning(request, "No se enviaron datos...")
        return HttpResponseRedirect(reverse("tienda:form_cat", args=()))


def eliminar_usuario(request, correo):
    if request.method == 'GET':
        usuario = get_object_or_404(Usuario, correo=correo)
        usuario.delete()
        messages.success(request, 'Usuario eliminado exitosamente.')
        return redirect('lista_usuarios')  
    else:
        return redirect('lista_usuarios')  


def admin_editar_formulario(request, correo):
    q = Usuario.objects.get(correo=correo)
    contexto = {"id": correo, "data": q}
    return render(request, 'ourschool/perfil.html', contexto)


def perfil(request):
    usuario = request.session.get("logueo", False)
    q = Usuario.objects.get(correo=usuario['correo'])
    contexto = {"data": q}
    return render(request, "ourschool/perfil.html", contexto)

def guardar_cambios_usuario(request, correo):
    if request.method == "POST":
        usuario = Usuario.objects.get(correo=correo)
        usuario.nombre_apellido = request.POST.get('nombre_apellido')
        usuario.correo = request.POST.get('correo')
        usuario.contrasena = request.POST.get('contrasena')
        usuario.telefono = request.POST.get('telefono')
        usuario.save()
        return redirect('inicio_estudiante')  
    else:
        return redirect('inicio_estudiante')  


def agregar_mensaje(request):
    return render(request, 'ourschool/agregar_mensaje.html')


def formulario_mensaje(request):
    enviado = False
    if request.method == "POST":
        descripcion = request.POST.get("descripcion")
        mensaje = Mensaje(descripcion=descripcion)
        mensaje.save()
        enviado = True

    return render(request, 'ourschool/formulario_mensaje.html', {'enviado': enviado})


def inicio_profesor(request):
    mensajes = Mensaje.objects.all()  
    return render(request, 'ourschool/inicio_profesor.html', {'mensajes': mensajes})


def mensajes_profesor(request):
    mensajes = Mensaje.objects.all()  
    return render(request, 'ourschool/mensajes_profesor.html', {'mensajes': mensajes})


def eliminar_mensaje(request, mensaje_id):
    if request.method == "POST":
        mensaje = get_object_or_404(Mensaje, id=mensaje_id)
        mensaje.delete()
        return redirect('mensajes_profesor')  