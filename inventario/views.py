from django.shortcuts import render, redirect
#importacion de vistas genericas
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages

#importar el auth de django
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required, permission_required
#importacion de los modelos cateroria
from .models import Categoria, SubCategoria, Marca, UnidadMedida, Producto
from .forms import CategoriaForm, SubCategoriaForm, MarcaForm, UMForm, ProductoForm

from bases.views import SinPrivilegios

# Create your views here.
class CategoriaView(SinPrivilegios, generic.ListView):
  permission_required = "inventario.view_categoria"
  model = Categoria
  template_name = "inventario/categoria_list.html"
  context_object_name = "obj"



class CategoriaNew(SuccessMessageMixin, SinPrivilegios, generic.CreateView):
  permission_required="inventario.add_categoria"
  model = Categoria
  template_name = "inventario/categoria_form.html"
  context_object_name = "obj"
  form_class=CategoriaForm
  success_url=reverse_lazy("inv:categoria_list")
  success_message="Categoria Creada Satisfactoriamente"

  def form_valid(self, form):
      form.instance.usuarioCreado = self.request.user
      return super().form_valid(form)
  

class CategoriaEdit(SuccessMessageMixin, SinPrivilegios,  generic.UpdateView):
    permission_required="inventario.chance_categoria"
    model=Categoria
    template_name="inventario/categoria_form.html"
    context_object_name = "obj"
    form_class=CategoriaForm
    success_url=reverse_lazy("inv:categoria_list")
    success_message="Categoria Actualizada Satisfactoriamente"

    def form_valid(self, form):
        form.instance.fechaModificada = self.request.user.id
        return super().form_valid(form)
    
class CategoriaDel(SuccessMessageMixin, SinPrivilegios,  generic.DeleteView):
   permission_required="inventario.delete_categoria"
   model = Categoria
   template_name='inventario/catalogos_del.html'
   context_object_name='obj'
   success_url=reverse_lazy("inv:categoria_list")
   success_message="Categoría Eliminada Satisfactoriamente"

#vistas de subcategoria
class SubCategoriaView(SinPrivilegios, generic.ListView):
    permission_required = "inventario.view_subcategoria"
    model = SubCategoria
    template_name = "inventario/subcategoria_list.html"
    context_object_name = "obj"
    


class SubCategoriaNew(SuccessMessageMixin, SinPrivilegios, generic.CreateView):
    permission_required = "inventario.add_subcategoria"
    model=SubCategoria
    template_name="inventario/subcategoria_form.html"
    context_object_name = "obj"
    form_class=SubCategoriaForm
    success_url=reverse_lazy("inv:subcategoria_list")
    success_message="Sub Categoría Creada Satisfactoriamente"
   

    def form_valid(self, form):
        form.instance.usuarioCreado = self.request.user
        return super().form_valid(form)
    

class SubCategoriaEdit(SuccessMessageMixin, SinPrivilegios,  generic.UpdateView):
    permission_required = "inventario.chage_subcategoria"
    model=SubCategoria
    template_name="inventario/subcategoria_form.html"
    context_object_name = "obj"
    form_class=SubCategoriaForm
    success_url=reverse_lazy("inventario:subcategoria_list")
    success_message="Sub Categoría Actualizada Satisfactoriamente"

    def form_valid(self, form):
        form.instance.usuarioModificado = self.request.user.id
        return super().form_valid(form)
    

class SubCategoriaDel(SuccessMessageMixin, SinPrivilegios,  generic.DeleteView):
    permission_required="inv.delete_subcategoria"
    model=SubCategoria
    template_name='inventario/catalogos_del.html'
    context_object_name='obj'
    success_message="Sub Categoría Eliminada"
    success_url=reverse_lazy("inventario:subcategoria_list")


class MarcaView(SinPrivilegios, generic.ListView):
    permission_required = "inventario.view_marca"
    model = Marca
    template_name = "inventario/marca_list.html"
    context_object_name = "obj"
    


class MarcaNew(SuccessMessageMixin, SinPrivilegios, generic.CreateView):
         permission_required="inventario.add_marca"
         model= Marca
         template_name = 'inventario/marca_form.html'
         context_object_name = 'obj'
         form_class = MarcaForm
         success_url= reverse_lazy("inventario:marca_list")
         success_message="Marca Creada"

         def form_valid(self, form):
          form.instance.usuarioCreado = self.request.user
          return super().form_valid(form)

    
class MarcaEdit(SuccessMessageMixin, SinPrivilegios, generic.UpdateView):
    permission_required="inv.change_marca"
    model=Marca
    template_name="inventario/marca_form.html"
    context_object_name = 'obj'
    form_class=MarcaForm
    success_url= reverse_lazy("inventario:marca_list")
    success_message="Marca Editada"
 

    def form_valid(self, form):
        form.instance.usuarioModificado = self.request.user.id
        return super().form_valid(form)


@login_required(login_url='/login/')
@permission_required('inv.change_marca', login_url='bases:sin_privilegios')
def marca_inactivar(request, id):
    marca = Marca.objects.filter(pk=id).first()
    contexto={}
    template_name="inv/catalogos_del.html"


    if not marca:
        return redirect("inv:marca_list")
    
    if request.method=='GET':
        contexto={'obj':marca}
    
    if request.method=='POST':
        marca.estado=False
        marca.save()
        messages.success(request, 'Marca Inactivada')
        return redirect("inv:marca_list")

    return render(request,template_name,contexto)


class UMView(SinPrivilegios, generic.ListView):
    model = UnidadMedida
    template_name = "inv/um_list.html"
    context_object_name = "obj"
    permission_required="inv.view_unidadmedida"


class UMNew(SuccessMessageMixin,SinPrivilegios,
                   generic.CreateView):
    model=UnidadMedida
    template_name="inv/um_form.html"
    context_object_name = 'obj'
    form_class=UMForm
    success_url= reverse_lazy("inv:um_list")
    success_message="Unidad Medida Creada"
    permission_required="inv.add_unidadmedida"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        print(self.request.user.id)
        return super().form_valid(form)


class UMEdit(SuccessMessageMixin,SinPrivilegios,
                   generic.UpdateView):
    model=UnidadMedida
    template_name="inv/um_form.html"
    context_object_name = 'obj'
    form_class=UMForm
    success_url= reverse_lazy("inv:um_list")
    success_message="Unidad Medida Editada"
    permission_required="inv.change_unidadmedida"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        print(self.request.user.id)
        return super().form_valid(form)


@login_required(login_url="/login/")
@permission_required("inv.change_unidadmedida",login_url="/login/")
def um_inactivar(request, id):
    um = UnidadMedida.objects.filter(pk=id).first()
    contexto={}
    template_name="inv/catalogos_del.html"

    if not um:
        return redirect("inv:um_list")
    
    if request.method=='GET':
        contexto={'obj':um}
    
    if request.method=='POST':
        um.estado=False
        um.save()
        return redirect("inv:um_list")

    return render(request,template_name,contexto)


class ProductoView(SinPrivilegios, generic.ListView):
    model = Producto
    template_name = "inv/prducto_list.html"
    context_object_name = "obj"
    permission_required="inv.view_producto"


class ProductoNew(SuccessMessageMixin,SinPrivilegios,
                   generic.CreateView):
    model=Producto
    template_name="inv/producto_form.html"
    context_object_name = 'obj'
    form_class=ProductoForm
    success_url= reverse_lazy("inv:producto_list")
    success_message="Producto Creado"
    permission_required="inv.add_producto"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super(ProductoNew, self).get_context_data(**kwargs)
        context["categorias"] = Categoria.objects.all()
        context["subcategorias"] = SubCategoria.objects.all()
        return context



class ProductoEdit(SuccessMessageMixin,SinPrivilegios,
                   generic.UpdateView):
    model=Producto
    template_name="inv/producto_form.html"
    context_object_name = 'obj'
    form_class=ProductoForm
    success_url= reverse_lazy("inv:producto_list")
    success_message="Producto Editado"
    permission_required="inv.change_producto"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')

        context = super(ProductoEdit, self).get_context_data(**kwargs)
        context["categorias"] = Categoria.objects.all()
        context["subcategorias"] = SubCategoria.objects.all()
        context["obj"] = Producto.objects.filter(pk=pk).first()

        return context


@login_required(login_url="/login/")
@permission_required("inv.change_producto",login_url="/login/")
def producto_inactivar(request, id):
    prod = Producto.objects.filter(pk=id).first()
    contexto={}
    template_name="inv/catalogos_del.html"

    if not prod:
        return redirect("inv:producto_list")
    
    if request.method=='GET':
        contexto={'obj':prod}
    
    if request.method=='POST':
        prod.estado=False
        prod.save()
        return redirect("inv:producto_list")

    return render(request,template_name,contexto)