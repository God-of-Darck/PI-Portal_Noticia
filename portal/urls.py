from django.urls import path
from . import views

urlpatterns = [
    path('', views.TodasNoticias, name='noticias'),
    path('noticia/<int:id>', views.noticia, name='noticia-views'),
    path('politicas/', views.politicas, name='politica-views'),
    path('sobrenos/', views.sobrenos, name='sobreno-views'),
    path('ia/', views.ia, name='ia-views'),
    path('ti/', views.ti, name='ti-views'),
    path('games/', views.games, name='games-views'),
    path('robotica/', views.robotk, name='robotk-views'),
    
]