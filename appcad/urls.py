from django.urls import path
from . import views

app_name= 'usuarios'

urlpatterns = [
    path('cadastrara/', views.cad_view, name='criar')
]