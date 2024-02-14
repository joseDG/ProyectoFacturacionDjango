from django.shortcuts import render
#importacion de vistas genericas
from django.views import generic
from django.urls import reverse_lazy
#importar el auth de django
from django.contrib.auth.mixins import LoginRequiredMixin
#importacion de los modelos cateroria
from .models import Categoria
from .forms import CategoriaForm

# Create your views here.
class CategoriaView(LoginRequiredMixin, generic.ListView):
  model = Categoria
  template_name = "inventario/categoria_list.html"
  context_object_name = "obj"
  login_url = 'bases:login'


class CategoriaNew(LoginRequiredMixin, generic.CreateView):
  model = Categoria
  template_name = "inventario/categoria_form.html"
  context_object_name = "obj"
  form_class=CategoriaForm
  success_url=reverse_lazy('inventario:categoria_list')
  login_url="bases:login"

  def form_valid(self, form):
      form.instance.usuarioCreado = self.request.user
      return super().form_valid(form)
  
