from django.shortcuts import render
# views
from django.views.generic import ListView, TemplateView
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

class PersonListView(TemplateView):

    template_name = 'persona/lista.html'

class PersonSearchApiView(ListAPIView):

    # Serializador
    serializer_class = PersonSerializers

    def get_queryset(self):
        # obtener parametro de la url
        param = self.kwargs['termino']
        return Person.objects.filter(
            full_name__icontains=param
        )
