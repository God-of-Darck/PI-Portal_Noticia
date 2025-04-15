from django.db import models

# Create your models here.

class Noticias(models.Model):
  
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()  # Campo de descrição
    imagem = models.ImageField(upload_to='uploads_img/', null=False, blank=False)  # Campo de imagem
    noticia = models.TextField()  # Conteúdo completo da notícia
    
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo