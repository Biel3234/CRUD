from django.urls import path
from . import views

app_name= 'usuarios'

urlpatterns = [
    path('cadastrara/', views.cad_view, name='criar'),
    path('lista/', views.mostrar_view, name='lista'),
    path('atualizar/<int:pk>/', views.atualizar_view , name='atualizar'),
    path('deletar/<int:pk>/', views.deletar_view, name='deletar')
]