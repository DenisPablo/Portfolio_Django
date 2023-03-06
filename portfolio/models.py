from django.db import models
from django.db.models.fields import URLField
from django.db.models.fields.files import ImageField

# Create your models here.


class Proyecto(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    f_publicado = models.DateTimeField(auto_now_add=True)
    tecnologias = models.CharField(max_length=200)
    imagenes = ImageField(upload_to="portfolio/imagenes/")
    url = URLField(blank=True)
