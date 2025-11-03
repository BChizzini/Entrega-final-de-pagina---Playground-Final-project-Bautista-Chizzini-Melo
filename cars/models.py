from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Car(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    descripcion = RichTextField()
    imagen = models.ImageField(upload_to='cars/')
    fecha_publicacion = models.DateField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.marca} {self.modelo}"
