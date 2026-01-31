from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro/', views.cadastrar_pet, name='cadastrar_pet'),
    path('lista/', views.lista_pets, name='lista_pets'),
    path('excluir/<int:id>/', views.excluir_pet, name='excluir_pet'),
    path('editar/<int:id>/', views.editar_pet, name='editar_pet'),
]