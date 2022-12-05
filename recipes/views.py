from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Usando o argumento context, é possível enviar variáveis para a template especificada.
def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name':'Luiz Fernando Sementille',
    }) 