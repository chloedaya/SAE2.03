from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Films, Acteurs, Categories, Personnes, Commentaires, FilmsActeurs

# FILMS
def seefilms(request):
    films = Films.objects.all()
    return render(request, 'seefilm/films.html', {'films': films})

# ACTEURS
def seeacteurs(request):
    acteurs = Acteurs.objects.all()
    return render(request, 'seefilm/acteurs.html', {'acteurs': acteurs})

# CATEGORIES
def seecategories(request):
    categories = Categories.objects.all()
    return render(request, 'seefilm/categories.html', {'categories': categories})

# PERSONNES
def seepersonnes(request):
    personnes = Personnes.objects.all()
    return render(request, 'seefilm/personnes.html', {'personnes': personnes})

# COMMENTAIRES
def seecommentaires(request):
    commentaires = Commentaires.objects.all()
    return render(request, 'seefilm/commentaires.html', {'commentaires': commentaires})

# FILMS-ACTEURS (table de liaison)
def seefilmsacteurs(request):
    filmsacteurs = FilmsActeurs.objects.all()
    return render(request, 'seefilm/filmsacteurs.html', {'filmsacteurs': filmsacteurs})
