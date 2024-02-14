from django.shortcuts import render
#importacion de vistas genericas
from django.views import generic
#importar el auth de django
from django.contrib.auth.mixins import LoginRequiredMixin
#importacion de los modelos cateroria
from .models import Categoria

# Create your views here.
class CategoriaView(LoginRequiredMixin, generic.ListView):
  model = Categoria
  template_name = "inventario/categoria_list.html"
  context_object_name = "obj"
  login_url = 'bases:login'
