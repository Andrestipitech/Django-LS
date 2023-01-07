from django.shortcuts import render, redirect
from apps.pbv.forms import prueba
from apps.pbv.models import pbv
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
def saludoP(request):
    return render(request, 'boostrap/conf_delet.html')

def insertar_pbv(request):
    if request.method == 'POST':
        form = prueba(request.POST)
        if form.is_valid():
            form.save()
        return redirect('pbv:index')
    else:
        form = prueba()
    return render(request, 'boostrap/index.html', {'form': form})

def pbv_list(request):
    pbv_lista = pbv.objects.all()
    contexto = {'pbv':pbv_lista}
    return render(request, 'boostrap/index.html', contexto)

class crear_listar(CreateView):
    model = pbv
    template_name = 'boostrap/index.html'
    form_class = prueba
    success_url = reverse_lazy('pbv:lista')

    def get_context_data(self, **kwargs):
        context = super(crear_listar, self).get_context_data(**kwargs)
        #context['form'] = self.form_class(self.request.GET)
        context['form'] = self.form_class()
        context['pbv'] =  pbv.objects.all()
        return context

def pbv_delete(request, id_pbv):
    obj_pbv = pbv.objects.get(idpbv=id_pbv)
    if request.method == 'POST':
        obj_pbv.delete()
        return redirect('pbv:lista')
    return render(request, 'boostrap/conf_delet.html', {'pbv': obj_pbv})

class Pbv_editar(UpdateView):
    model = pbv
    form_class = prueba
    template_name ='boostrap/edit_pbv.html'
    success_url = reverse_lazy('pbv:lista')

def pbv_editar(request, id_pbv):
    obj_pbv = pbv.objects.get(idpbv=id_pbv)
    if request.method == 'GET':
        form = prueba(instance=obj_pbv)
    else:
        form = prueba(request.POST, instance=obj_pbv)
        if form.is_valid():
            form.save()
        return  redirect('pbv:lista')
    return render(request, 'boostrap/edit_pbv.html', {'form':form})