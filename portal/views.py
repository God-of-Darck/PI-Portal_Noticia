from django.shortcuts import render, get_object_or_404, redirect
from .models import Noticias

# Create your views here.
def TodasNoticias(request):
    Noticias_Todas = Noticias.objects.all().order_by('-created_at')
    return render(request, 'portal/noticias.html', {'Noticias_Todas': Noticias_Todas})
