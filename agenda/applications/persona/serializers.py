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