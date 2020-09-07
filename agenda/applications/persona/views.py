from django.shortcuts import render
# views
from django.views.generic import ListView
# models
from .models  import Person

class ListaPersona(ListView):
    
    template_name = 'persona/personas.html'
    context_object_name = 'listaPersona'

    def get_queryset(self):
        
        return Person.objects.all()


