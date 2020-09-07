# serializers
from rest_framework import serializers
# models
from .models import Person, Reunion

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

class PersonSerializers2(serializers.ModelSerializer):

    # Activo, es un campo no obligatorio y que se mostrara a pesar de no ser parte del modelo
    activo = serializers.BooleanField(default=False)

    class Meta:
        # Definir modelo a serializar
        model = Person
        # Definir campos del modelo a serializar, podria utlizar __all__ para especificar todos los campos
        '''
        fields = (
            'id',
            'full_name',
        )
        '''
        fields = ('__all__')

class ReunionSerializers(serializers.ModelSerializer):
    
    # con esto le diremos al serializador que en su campo 'persona' que es una clave foranea
    # Utilice el serializador de Persona antes definido para que nos muestre los datos de la persona relacionada
    persona = PersonaSerializer() 
    
    class Meta:
        # Definir modelo
        model = Reunion
        # Definir campos del modelo, con __all__ mostramos todo 
        # fields= ('__all__')
        fields = (
            'id',
            'persona',
            'fecha',
            'hora',
            'asunto'
        )
