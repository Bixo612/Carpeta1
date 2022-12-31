from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import MensajeSerializador
from api_rest.models import Mensaje
from rest_framework import status
from django.http import Http404

# Create your views here.

class Mensaje_APIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        mensaje = Mensaje.objects.all()
        serializador = MensajeSerializador(mensaje, many=True)

        return Response(serializador.data)
    
    def post(self, request, format=None):
        serializador = MensajeSerializador(data=request.data)
        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data, status=status.HTTP_201_CREATED)
        return Response(serializador.data, status=status.HTTP_400_BAD_REQUEST)

class Mensaje_APIView_Detail(APIView):
    def get_object(self, pk):
        try:
            return Mensaje.objects.get(pk=pk)
        except Mensaje.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        mensaje = self.get_object(pk)
        serializador = MensajeSerializador(mensaje)
        return Response(serializador.data)

    def put(self, request, pk, format = None):
        mensaje = self.get_object(pk)
        serializador = MensajeSerializador(mensaje, data=request.data)
        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data)
        return Response(serializador.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        mensaje = self.get_object(pk)
        mensaje.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



