from django.shortcuts import render, get_object_or_404, redirect
from .models import Noticias


def TodasNoticias(request):
    Noticias_Todas = Noticias.objects.all().order_by('-created_at')
    return render(request, 'portal/noticias.html', {'Noticias_Todas': Noticias_Todas})


def noticia(request, id):
    noticia = get_object_or_404(Noticias, pk=id)
    return render(request, 'portal/noticia.html', {'noticia': noticia})