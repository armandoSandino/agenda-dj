from django.db import models
# 
from django.db.models import Count

class ReunionManager(models.Manager):

    def cantidad_de_reuniones_por_trabajo(self):

        resultado = self.values(
            'persona__job'
        ).annotate(
            cantidad_total_reunion=Count('id')
        )

        return resultado