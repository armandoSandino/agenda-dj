# serializers
from rest_framework import serializers, pagination

from rest_framework.pagination import PageNumberPagination

# models
from .models import Person, Reunion, Hobby

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

class HobbySerializers(serializers.ModelSerializer):

    class Meta:
        # definir el modelo
        model = Hobby
        # definir campos
        fields = (
            'id',
            'hobby',
            'created'
        )

class PersonSerializers3(serializers.ModelSerializer):

    # con esto le diremos al serializador que en su campo 'hobbies' que es una clave foranea de una relacion many to many
    # Utilice el serializador de Hobbies antes definido para que nos muestre los datos relacionados
    # many=True, le indicamos que se especificara una coleccio y no solo un elemento
    hobbies = HobbySerializers(many=True)
    
    class Meta:
        # Definir modelo a serializar
        model = Person
        # Definir campos del modelo a serializar, podria utlizar __all__ para especificar todos los campos
        fields = (
            'id',
            'full_name',
            'job',
            'email',
            'phone',
            'hobbies',
            'created',
        )
class ReunionSerializers2(serializers.ModelSerializer):

    # son campo no obligatorio y que se mostrara a pesar de no ser parte del modelo
    
    activo = serializers.BooleanField(default=False)
    # SerializerMethodField, indica que su valor se obtendra del resultado de algunua operacion en una funcion
    fecha_hora = serializers.SerializerMethodField( )
    
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
            'asunto',
            
            'activo',
            'fecha_hora'
        )
    
    def get_fecha_hora(self, obj ):
        
        return str(obj.fecha) + '-'+ str(obj.hora)


class ReunionSerializerLink(serializers.HyperlinkedModelSerializer):

      
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
            'asunto',
        )
        # view_name, indica la vista que deseamos cargar para el campo persona(ForeignKey)
        # Dicha vista a ser invocada siempre debe ser un RetrieveAPIView/DetailView
        # lookup_field, recibe los paremetros de la ruta a invocar el 'pk' esta definido en las rutas
        extra_kwargs = {
            'persona': {
                'view_name': 'persona_app:person-detail',
                'lookup_field': 'pk'
            }
        }
        

class PersonPagination(pagination.PageNumberPagination):
    page_size = 5
    max_page_size = 10

class CountReunionSerialiazer(serializers.Serializer):

    persona__job = serializers.CharField()
    cantidad_total_reunion = serializers.IntegerField()