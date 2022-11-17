from django.shortcuts import render

def inicio(request):
    request.session['usuario'] = 'Usuario Prueba'
    variableS = request.session['usuario']
    return render(request,'inicio.html',{'mensaje':variableS})