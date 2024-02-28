from django.shortcuts import render, redirect
#importacion de vistas genericas
from django.views import generic
from django.urls import reverse_lazy
#importar el auth de django
from django.contrib.auth.mixins import LoginRequiredMixin
#importacion de los modelos cateroria
from .models import Categoria, SubCategoria, Marca, UnidadMedida, Producto
from .forms import CategoriaForm, SubCategoriaForm, MarcaForm, UMForm, ProductoForm

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


class UMView(LoginRequiredMixin, generic.ListView):
    model = UnidadMedida
    template_name = "inventario/um_list.html"
    context_object_name = "obj"
    #permission_required="inv.view_unidadmedida"

class UMNew(LoginRequiredMixin, generic.CreateView):
    model=UnidadMedida
    template_name="inventario/um_form.html"
    context_object_name = 'obj'
    form_class=UMForm
    success_url= reverse_lazy("inventario:um_list")
    success_message="Unidad Medida Creada"
    #permission_required="inv.add_unidadmedida"

    def form_valid(self, form):
        form.instance.usuarioCreado = self.request.user
        print(self.request.user.id)
        return super().form_valid(form)


class UMEdit(LoginRequiredMixin, generic.UpdateView):
    model=UnidadMedida
    template_name="inventario/um_form.html"
    context_object_name = 'obj'
    form_class=UMForm
    success_url= reverse_lazy("inventario:um_list")
    success_message="Unidad Medida Editada"
    #permission_required="inv.change_unidadmedida"

    def form_valid(self, form):
        form.instance.usuarioModificado = self.request.user.id
        print(self.request.user.id)
        return super().form_valid(form)

def um_inactivar(request, id):
    um = UnidadMedida.objects.filter(pk=id).first()
    contexto={}
    template_name="inventario/catalogos_del.html"

    if not um:
        return redirect("inventario:um_list")
    
    if request.method=='GET':
        contexto={'obj':um}
    
    if request.method=='POST':
        um.estado=False
        um.save()
        return redirect("inventario:um_list")

    return render(request,template_name,contexto)


class ProductoView(LoginRequiredMixin, generic.ListView):
    model = Producto
    template_name = "inventario/prducto_list.html"
    context_object_name = "obj"
    #permission_required="inv.view_producto"


class ProductoNew(LoginRequiredMixin, generic.CreateView):
    model=Producto
    template_name="inventario/producto_form.html"
    context_object_name = 'obj'
    form_class=ProductoForm
    success_url= reverse_lazy("inventario:producto_list")
    #success_message="Producto Creado"
    #permission_required="inv.add_producto"

    def form_valid(self, form):
        form.instance.usuarioCreado = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super(ProductoNew, self).get_context_data(**kwargs)
        context["categorias"] = Categoria.objects.all()
        context["subcategorias"] = SubCategoria.objects.all()
        return context



class ProductoEdit(LoginRequiredMixin, generic.UpdateView):
    model=Producto
    template_name="inventario/producto_form.html"
    context_object_name = 'obj'
    form_class=ProductoForm
    success_url= reverse_lazy("inventario:producto_list")
    #success_message="Producto Editado"
    #permission_required="inv.change_producto"

    def form_valid(self, form):
        form.instance.usuarioModificado = self.request.user.id
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')

        context = super(ProductoEdit, self).get_context_data(**kwargs)
        context["categorias"] = Categoria.objects.all()
        context["subcategorias"] = SubCategoria.objects.all()
        context["obj"] = Producto.objects.filter(pk=pk).first()

        return context



def producto_inactivar(request, id):
    prod = Producto.objects.filter(pk=id).first()
    contexto={}
    template_name="inventario/catalogos_del.html"

    if not prod:
        return redirect("inventario:producto_list")
    
    if request.method=='GET':
        contexto={'obj':prod}
    
    if request.method=='POST':
        prod.estado=False
        prod.save()
        return redirect("inventario:producto_list")

    return render(request,template_name,contexto)