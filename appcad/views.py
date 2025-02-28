from django.shortcuts import render, redirect
from .forms import FormCad
from .models import Usuario

def cad_view(request):
    if request.method == 'GET':
        form = FormCad
        return render(request, 'cadastrar.html', {'form': form})
    elif request.method == 'POST':
            form = FormCad(request.POST)
            form.save()
            return redirect('usuarios:criar')
        
def mostrar_view(request):
    usuarios = Usuario.objects.all()
    if usuarios:
        return render(request, 'list.html', {'usuarios': usuarios})
    
def atualizar_view(request, pk):
    usuario = Usuario.objects.get(pk = pk)
    if request.method == 'POST':
        form = FormCad(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('usuarios:lista')
    else:
        form = FormCad(instance=usuario)
    return render(request, 'atualizar.html', {'form': form, 'usuario': usuario})

def deletar_view(request, pk):
    usuario = Usuario.objects.get(pk = pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('usuarios:lista')
    else:
        return render(request, 'confirmar.html', {'usuario': usuario})
    