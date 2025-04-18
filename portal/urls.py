from django.urls import path
from . import views

urlpatterns = [
    path('', views.TodasNoticias, name='noticias'),
    path('noticia/<int:id>', views.noticia, name='noticia-views'),
    path('politicas/', views.politicas, name='politica-views'),
    path('sobrenos/', views.sobrenos, name='sobreno-views'),
    
]