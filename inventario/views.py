from django.shortcuts import render
#importacion de vistas genericas
from django.views import generic
from django.urls import reverse_lazy
#importar el auth de django
from django.contrib.auth.mixins import LoginRequiredMixin
#importacion de los modelos cateroria
from .models import Categoria, SubCategoria
from .forms import CategoriaForm, SubCategoriaForm

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
  

class CategoriaEdit(LoginRequiredMixin, generic.UpdateView):
    model=Categoria
    template_name="inventario/categoria_form.html"
    context_object_name = "obj"
    form_class=CategoriaForm
    success_url=reverse_lazy("inventario:categoria_list")
    login_url="bases:login"

    def form_valid(self, form):
        form.instance.fechaModificada = self.request.user.id
        return super().form_valid(form)
    
class CategoriaDel(LoginRequiredMixin, generic.DeleteView):
   model = Categoria
   template_name='inventario/catalogos_del.html'
   context_object_name='obj'
   success_url=reverse_lazy("inventario:categoria_list")

#vistas de subcategoria
class SubCategoriaView(LoginRequiredMixin, generic.ListView):
    model = SubCategoria
    template_name = "inventario/subcategoria_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'


class SubCategoriaNew(LoginRequiredMixin, generic.CreateView):
    model=SubCategoria
    template_name="inventario/subcategoria_form.html"
    context_object_name = "obj"
    form_class=SubCategoriaForm
    success_url=reverse_lazy("inventario:subcategoria_list")
    login_url = 'bases:login'
   

    def form_valid(self, form):
        form.instance.usuarioCreado = self.request.user
        return super().form_valid(form)
    
class SubCategoriaEdit(LoginRequiredMixin, generic.UpdateView):
    model=SubCategoria
    template_name="inventario/subcategoria_form.html"
    context_object_name = "obj"
    form_class=SubCategoriaForm
    success_url=reverse_lazy("inventario:subcategoria_list")
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.usuarioModificado = self.request.user.id
        return super().form_valid(form)
    

class SubCategoriaDel(LoginRequiredMixin, generic.DeleteView):
    model=SubCategoria
    template_name='inventario/catalogos_del.html'
    context_object_name='obj'
    success_url=reverse_lazy("inventario:subcategoria_list")
    
