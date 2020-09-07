from django.shortcuts import render
# views
from django.views.generic import ListView, TemplateView
# views drf
# RetrieveAPIView es equivalente al DetailView de Django
# DestroyAPIView  es equivalente al DeleteView de Django
# UpdateAPIView es equivalente al UpdateView en Django
# RetrieveUpdateAPIView, para que obtenga los datos a actualizar
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView,
)
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

class PersonCreateAPIView(CreateAPIView):

    # Definir el serializador
    serializer_class = PersonSerializers

# RetrieveAPIView es equivalente al DetailView de Django
class PersonRetrieveAPIView(RetrieveAPIView):

    # Definir el serializador
    serializer_class = PersonSerializers
    # Con el queryset puedes omitir la funcion get_queryset
    # queryset = Person.objects.all()

    def get_queryset(self):
        # Obtener los parametros pasados por el URL
        ID = self.kwargs['pk']
        # Puedes pasarle el parametro ID de usuario recibido por el url 
        # pero Django Rest framework lo detecta implicitamente
        return Person.objects.filter(
        )
       
# DestroyAPIView  es equivalente al DeleteView de Django
class DestroyAPIView(DestroyAPIView):
    
    # Definir el serializador
    serializer_class = PersonSerializers
    # Definir el queryset
    queryset = Person.objects.all()

# UpdateAPIView es equivalente al UpdateView en Django
class PersonUpdateView(UpdateAPIView ):

    # Definir el serializador
    serializer_class= PersonSerializers

# RetrieveUpdateAPIView es equivalente al UpdateView y DetailView en Django
class PersonRetrieveUpdateView(RetrieveUpdateAPIView ):

    # Definir el serializador
    serializer_class= PersonSerializers
    # Deinfir queryset
    queryset = Person.objects.all()