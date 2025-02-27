from django.shortcuts import render, redirect
from .forms import FormCad

def cad_view(request):
    if request.method == 'GET':
        form = FormCad
        return render(request, 'cadastrar.html', {'form': form})
    elif request.method == 'POST':
        form = FormCad(request.POST)
        form.save()
        return redirect('usuarios:criar')
    