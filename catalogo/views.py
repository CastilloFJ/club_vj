from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from datetime import timedelta, date
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, LogoutView
from .models import *
from django.db.models import Q
from datetime import datetime


# Create your views here.
def index(request):
    context = {}
    return render(request, 'index.html', context)


@login_required
def videojuegos(request):
    vj = VideoJuego.objects.select_related('plataforma', 'genero').all()

    # Parámetros
    q_query = request.GET.get('titulo')
    q_annio = request.GET.get('annio')
    q_plataforma = request.GET.get('plataforma')
    q_genero = request.GET.get('genero')
    

    # Búsqueda Inteligente: Si hay texto, busca en Título O en la descripción (si tuvieras)
    if q_query:
        vj = vj.filter(Q(titulo__icontains=q_query) | Q(annio__icontains=q_query))

    # Filtros exactos de selección
    if q_annio:
        vj = vj.filter(annio=q_annio)
    if q_plataforma:
        vj = vj.filter(plataforma__nombre=q_plataforma)
    if q_genero:
        vj = vj.filter(genero__nombre=q_genero)

    context = {
        'videojuegos': vj,
        'annios': VideoJuego.objects.values_list('annio', flat=True).distinct().order_by('-annio'),
        'generos': Genero.objects.all(),
        'plataformas': Plataforma.objects.all(),
        'annio_actual': datetime.now().year,
    }
    return render(request, 'videojuegos.html', context)


@login_required
def videojuego_detalle(request, id):
    vj = get_object_or_404(VideoJuego, id=id)
    vj = VideoJuego.objects.select_related('plataforma', 'genero').filter(id=id).first()
    print(vj)

    if vj.annio == datetime.now().year and not request.user.userprofile.vip:
            messages.warning(request, "Este juego es exclusivo para miembros VIP.")
            return redirect('videojuegos')

    context = {
        'detalle_vj': vj
    }
    return render(request, 'videojuego_detalle.html', context)


class RegisterView(View):
    def get(self, request):
        return render(request, 'registration/register.html')

    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        rut = request.POST.get('rut')
        direccion = request.POST.get('direccion')
        telefono = request.POST.get('telefono')

        # 1. Validar si el email (username) ya existe
        if User.objects.filter(username=email).exists():
            messages.error(request, 'El correo electrónico ya está registrado.')
            return render(request, 'registration/register.html')

        # 2. Validar si el RUT ya existe en UserProfile
        if UserProfile.objects.filter(rut=rut).exists():
            messages.error(request, 'El RUT ingresado ya se encuentra registrado.')
            return render(request, 'registration/register.html')


        if password1 != password2:
            messages.error(request, 'Passwords do not match')
            return redirect(reverse('register'))  
        
        user = User.objects.create_user(username=email, email=email, password=password1, first_name=first_name, last_name=last_name)
        #user.is_active = False
        UserProfile.objects.create(user=user, rut=rut, direccion=direccion, telefono=telefono, vip=False)
        user.save()
        user = authenticate(username=email, password=password1)
        if user is not None:
            login(request, user)
        messages.success(request, 'Usuario creado exitosamente')
        return redirect('index')
    
class CustomLoginView(SuccessMessageMixin, LoginView):
    success_message = "Sesion Iniciada Exitosamente"
    template_name = 'registration/login.html'  
    redirect_authenticated_user = True
    
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.add_message(request, messages.WARNING, "Sesion Cerrada Exitosamente")
        return response
    

def quienes_somos(request):
    return render(request, 'quienes_somos.html')


def preguntas_frecuentes(request):
    return render(request, 'preguntas_frecuentes.html')


def eventos(request):
    return render(request, 'eventos.html')