from django.db import models

# Create your models here.
class Services(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    sub_title = models.CharField(max_length=200, verbose_name="Subtitulo")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imagen", upload_to="services")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    

    class Meta:
        verbose_name = 'Servicios'
        verbose_name_plural = 'Servicios'
        ordering = ['-created']
    
    def __str__(self):
        return self.title