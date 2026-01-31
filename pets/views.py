from django.shortcuts import render, redirect
from .models import Pet
from django.shortcuts import get_object_or_404


def cadastrar_pet(request):
    if request.method == "POST":
        # Pegamos o que o usuário digitou no HTML
        Pet.objects.create(
            nome=request.POST.get('nome'),
            especie=request.POST.get('especie'),
            raca=request.POST.get('raca'),
            idade=request.POST.get('idade')
        )
        return redirect('lista_pets') # Vamos criar essa URL já já
    
    return render(request, 'pets/cadastro.html')

def lista_pets(request):
    pets = Pet.objects.all()
    return render(request, 'pets/lista.html', {'pets': pets})

def home(request):
    return render(request, 'pets/home.html')

def excluir_pet(request, id):
    pet = get_object_or_404(Pet, id=id)
    pet.delete()
    return redirect('lista_pets')

def editar_pet(request, id):
    pet = get_object_or_404(Pet, id=id)
    if request.method == "POST":
        pet.nome = request.POST.get('nome')
        pet.especie = request.POST.get('especie')
        pet.raca = request.POST.get('raca')
        pet.idade = request.POST.get('idade')
        pet.save()
        return redirect('lista_pets')
    return render(request, 'pets/editar.html', {'pet': pet})

def lista_pets(request):
    nome_pesquisa = request.GET.get('search') # Pega o que foi digitado na busca
    if nome_pesquisa:
        # Filtra pets cujo nome contenha o texto digitado (sem diferenciar maiúsculas/minúsculas)
        pets = Pet.objects.filter(nome__icontains=nome_pesquisa)
    else:
        pets = Pet.objects.all()
    
    return render(request, 'pets/lista.html', {'pets': pets})

def lista_pets(request):
    # Pega o termo digitado na barra de busca (se houver)
    nome_pesquisa = request.GET.get('search') 
    
    if nome_pesquisa:
        # Filtra os pets que contenham o nome pesquisado
        pets = Pet.objects.filter(nome__icontains=nome_pesquisa) 
    else:
        # Se não houver pesquisa, mostra todos como antes
        pets = Pet.objects.all() 
    
    return render(request, 'pets/lista.html', {'pets': pets})