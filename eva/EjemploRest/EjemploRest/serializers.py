from rest_framework import serializers
from api_rest.models import Mensaje

class MensajeSerializador(serializers.ModelSerializer):
    class Meta:
        model = Mensaje
        exclude = ['is_removed', 'created', 'modified'] #remover las acciones que no se deben conciderar
        