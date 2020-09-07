#
from model_utils.models import TimeStampedModel
#
from django.db import models
# Managers
from .managers import ReunionManager

class Hobby(TimeStampedModel):

    # Definir campos
    hobby = models.CharField(
        'Pasa tiempo',
        max_length=50,
        blank=False
    )

    class Meta:
        verbose_name = 'hobby'
        verbose_name_plural = 'Hobbies'
    
    def __str__(self):

        return self.hobby
#
class Person(TimeStampedModel):
    """  Modelo para registrar personas de una agenda  """

    full_name = models.CharField(
        'Nombres', 
        max_length=50,
    )
    job = models.CharField(
        'Trabajo', 
        max_length=30,
        blank=True
    )
    email = models.EmailField(
        blank=True, 
        null=True
    )
    phone = models.CharField(
        'telefono',
        max_length=15,
        blank=True,
    )
    # Relacion many to many,
    hobbies = models.ManyToManyField(Hobby)

    class Meta:

        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
    
    def __str__(self):
        return self.full_name


class Reunion(TimeStampedModel):
    """ Modelo para la reunion """
    # Clave foranea
    persona = models.ForeignKey(
        Person,
        on_delete=models.CASCADE
    )
    fecha = models.DateField(blank=False)
    hora = models.TimeField()
    asunto = models.CharField(
        'Asunto de la reunion',
        max_length=100,
        blank=False
    )
    # Deinfir el managers

    objects = ReunionManager()

    class Meta:
        verbose_name = 'Reunion'
        verbose_name_plural = 'Reuniones'
    
    def __str__(self):
        return self.asunto
    