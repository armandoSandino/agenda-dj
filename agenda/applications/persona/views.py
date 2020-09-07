from django.shortcuts import render
# views
from django.views.generic import ListView
# views drf
from rest_framework.generics import ListAPIView
# models
from .models  import Person
# serializers
from .serializers import PersonSerializers

class ListaPersona(ListView):
    
    template_name = 'persona/personas.html'
    context_object_name = 'listaPersona'

    def get_queryset(self):
        
        return Person.objects.all()

class PersonListAPIView(ListAPIView):

    # Definir el serializador
    serializer_class = PersonSerializers

    def get_queryset(self):

        return Person.objects.all()


