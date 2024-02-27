from django.shortcuts import render, redirect
#importacion de vistas genericas
from django.views import generic
from django.urls import reverse_lazy
#importar el auth de django
from django.contrib.auth.mixins import LoginRequiredMixin
#importacion de los modelos cateroria
from .models import Categoria, SubCategoria, Marca
from .forms import CategoriaForm, SubCategoriaForm, MarcaForm

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


class MarcaView(LoginRequiredMixin, generic.ListView):
    model = Marca
    template_name = "inventario/marca_list.html"
    context_object_name = "obj"
    login_url = "bases:login"


class MarcaNew(LoginRequiredMixin, generic.CreateView):
         model= Marca
         template_name = 'inventario/marca_form.html'
         context_object_name = 'obj'
         form_class = MarcaForm
         success_url= reverse_lazy("inventario:marca_list")
         login_url = "bases:login"

         def form_valid(self, form):
          form.instance.usuarioCreado = self.request.user
          return super().form_valid(form)

    
class MarcaEdit(LoginRequiredMixin, generic.UpdateView):
    model=Marca
    template_name="inventario/marca_form.html"
    context_object_name = 'obj'
    form_class=MarcaForm
    success_url= reverse_lazy("inventario:marca_list")
    success_message="Marca Editada"
    

    def form_valid(self, form):
        form.instance.usuarioModificado = self.request.user.id
        return super().form_valid(form)



def marca_inactivar(request, id):
    marca = Marca.objects.filter(pk=id).first()
    contexto={}
    template_name="inventario/catalogos_del.html"


    if not marca:
        return redirect("inventario:marca_list")
    
    if request.method=='GET':
        contexto={'obj':marca}
    
    if request.method=='POST':
        marca.estado=False
        marca.save()
        #messages.success(request, 'Marca Inactivada')
        return redirect("inventario:marca_list")

    return render(request,template_name,contexto)
