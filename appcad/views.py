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
    