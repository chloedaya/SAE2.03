from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Films, Acteurs, Categories, Personnes, Commentaires, FilmsActeurs


def seefilms(request):
    films = Films.objects.all()
    return render(request, 'seefilm/films.html', {'films': films})


def seeacteurs(request):
    acteurs = Acteurs.objects.all()
    return render(request, 'seefilm/acteurs.html', {'acteurs': acteurs})

def seecategories(request):
    categories = Categories.objects.all()
    return render(request, 'seefilm/categories.html', {'categories': categories})


def seepersonnes(request):
    personnes = Personnes.objects.all()
    return render(request, 'seefilm/personnes.html', {'personnes': personnes})


def seecommentaires(request):
    commentaires = Commentaires.objects.all()
    return render(request, 'seefilm/commentaires.html', {'commentaires': commentaires})


def seefilmsacteurs(request):
    filmsacteurs = FilmsActeurs.objects.all()
    return render(request, 'seefilm/filmsacteurs.html', {'filmsacteurs': filmsacteurs})

#allcommentaires
def all(request):
    liste_livre=list(models.Livres.objects.all())
    return render(request,"bibliotheque/all.html",{"liste_livre":liste_livre})
