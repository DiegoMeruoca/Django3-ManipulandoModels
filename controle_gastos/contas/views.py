from django.shortcuts import render

def home(request):
    return render(request, "contas/home.html")
'''Retorna um render permitindo renderizar um template , passando
como parametrosa request e o nome e caminho do template '''

def desafio(request):
    return render(request, "contas/desafio.html")
