# serializers
from rest_framework import serializers
# models
from .models import Person

class PersonSerializers(serializers.ModelSerializer):

    class Meta:
        # Definir modelo a serializar
        model = Person
        # Definir campos del modelo a serializar, podria utlizar __all__ para especificar todos los campos
        '''
        fields = (
            'id',
            'full_name',
            'job',
            'email'
        )
        '''
        fields = ('__all__')

# Definir un serializador no enlazado a un Modelo existente
class PersonaSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    full_name = serializers.CharField()
    job = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()
    # Activo, es un campo no obligatorio
    activo = serializers.BooleanField(required=False)