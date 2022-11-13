from django.shortcuts import render

def irInicio(request):
    return render(request,"inicio.html")

def irRegistro(request):
    return render(request,"registro.html")

def irLista(request):
    return render(request,"lista.html")