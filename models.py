# Importar la clase Model de Django
from django.db import models

# Definir el modelo Evento
class Evento(models.Model):
    # Campos del modelo
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()

    # Método __str__ para representar el objeto como una cadena legible
    def __str__(self):
        return self.titulo
