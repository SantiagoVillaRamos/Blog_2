from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='titulo')
    description = models.TextField(verbose_name='descripcion')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='creado el')

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title