from django.shortcuts import render, get_object_or_404, redirect
from .models import Noticias

def TodasNoticias(request):
    ia = Noticias.objects.filter(noticias="ia").order_by('-created_at')[:4]
    ti = Noticias.objects.filter(noticias="ti").order_by('-created_at')[:4]
    game = Noticias.objects.filter(noticias="games-jogos").order_by('-created_at')[:4]
    robot = Noticias.objects.filter(noticias="robotica").order_by('-created_at')[:4]

    ianew = Noticias.objects.filter(noticias="ia").order_by('-created_at')[:1]
    tinew = Noticias.objects.filter(noticias="ti").order_by('-created_at')[:1]
    gamenew = Noticias.objects.filter(noticias="games-jogos").order_by('-created_at')[:1]
    robotnew = Noticias.objects.filter(noticias="robotica").order_by('-created_at')[:1]

    search = request.GET.get('search')
    if search:
        Noticias_filter = Noticias.objects.filter(titulo__icontains=search)
        return render(request, 'portal/pesquisa.html', {'Noticias_Todas': Noticias_filter})
    else:
        return render(request, 'portal/noticias.html', {
            'ia': ia,
            'ti': ti,
            'game': game,
            'robot': robot,
            'ianew': ianew,
            'tinew': tinew,
            'gamenew': gamenew ,
            'robotnew': robotnew})
        
def ia(request):
    iaall = Noticias.objects.filter(noticias="ia").order_by('-created_at')
    return render (request, 'portal/IA.html', {'ia': iaall} )
def ti(request):
    tiall = Noticias.objects.filter(noticias="ti").order_by('-created_at')
    return render (request, 'portal/TI.html', {'ti': tiall} )
def games(request):
    gameall = Noticias.objects.filter(noticias="games-jogos").order_by('-created_at')
    return render (request, 'portal/Games.html', {'game': gameall} )
def robotk(request):
    robotall = Noticias.objects.filter(noticias="robotica").order_by('-created_at')
    return render (request, 'portal/Robotica.html', {'robot': robotall} )



def noticia(request, id):
    print("ID recebido:", id)
    noticia = get_object_or_404(Noticias, pk=id)
    return render(request, 'portal/noticia.html', {'noticia': noticia})



def politicas(request):
    return render(request, 'portal/politicas.html')

def sobrenos(request):
    return render(request, 'portal/sobrenos.html')