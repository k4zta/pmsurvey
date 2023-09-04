from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.contrib import messages
from tasks.models import Estudiante
from .forms import LoginForm  # Asegúrate de importar el formulario correcto
def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Autenticar al estudiante
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Iniciar sesión si las credenciales son válidas
            login(request, user)
            return redirect('estudiante/')  # Cambia 'inicio' por la URL de tu página de inicio
        else:
            messages.error(request, 'Código o grupo incorrecto. Por favor, inténtalo de nuevo.')

    return render(request, 'home.html')

def estudiante(request):
    user = request.user
    return render(request, "estudiantes.html", {'nombre': user.first_name})
