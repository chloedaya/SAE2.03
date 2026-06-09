from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .forms import CategoriesForm, ActeursForm, FilmsForm, CommentairesForm
from .models import Categories, Acteurs, Films, Commentaires
from .models import Films

#ACCUEIL


def accueil(request):
    films = Films.objects.all()

    return render(request, "seefilm/accueil.html", {
        "films": films
    })
#LES AJOUTS

def ajoutCommentaires(request):
    if request.method == "POST":
        form = CommentairesForm(request.POST)

        if form.is_valid():
            commentaire = form.save()
            return render(request, "seefilm/commentaireaffiche.html", {
                "commentaire": commentaire
            })
    else:
        form = CommentairesForm()

    return render(request, "seefilm/commentaireajout.html", {
        "form": form
    })

def ajoutCategories(request):
    if request.method == "POST":
        form = CategoriesForm(request.POST)

        if form.is_valid():
            categorie = form.save()
            return render(request, "seefilm/cataffiche.html", {
                "categorie": categorie
            })
    else:
        form = CategoriesForm()

    return render(request, "seefilm/catajout.html", {
        "form": form
    })

def ajoutActeurs(request):
    if request.method == "POST":
        form = ActeursForm(
            request.POST or None,
            request.FILES or None,
        )

        if form.is_valid():
            acteur = form.save()
            return render(request, "seefilm/acteuraffiche.html", {
                "acteur": acteur
            })
    else:
        form = ActeursForm()

    return render(request, "seefilm/acteurajout.html", {
        "form": form
    })

def ajoutFilms(request):
    if request.method == "POST":
        form = FilmsForm(request.POST, request.FILES)

        if form.is_valid():
            film = form.save(commit=False)
            film.save()
            form.save_m2m()  # ⭐ OBLIGATOIRE pour les acteurs

            return render(request, "seefilm/filmaffiche.html", {
                "film": film
            })

    else:
        form = FilmsForm()

    return render(request, "seefilm/filmajout.html", {
        "form": form
    })

#LES ALL
def allCommentaires(request):
    liste_commentaire = Commentaires.objects.all()

    return render(request, "seefilm/commentaires.html", {
        "liste_commentaire": liste_commentaire
    })

def allFilms(request):
    liste_film = Films.objects.all()

    return render(request, "seefilm/films.html", {
        "liste_film": liste_film
    })

def allCategories(request):
    liste_categorie = Categories.objects.all()

    return render(request, "seefilm/categories.html", {
        "liste_categorie": liste_categorie
    })
def allActeurs(request):
    liste_acteur = Acteurs.objects.all()

    return render(
        request,
        "seefilm/acteurs.html",
        {"liste_acteur": liste_acteur}
    )

#MODIFIER

def readCommentaires(request, id):
    commentaire = get_object_or_404(Commentaires, pk=id)

    return render(request, "seefilm/commentaireaffiche.html", {
        "commentaire": commentaire
    })

def readFilms(request, id):
    film = get_object_or_404(Films, pk=id)

    return render(request, "seefilm/filmaffiche.html", {
        "film": film
    })

def readCategories(request, id):
    categorie = get_object_or_404(Categories, pk=id)

    return render(request, "seefilm/cataffiche.html", {
        "categorie": categorie
    })

#UPDATE

def updateCommentaires(request, id):
    commentaire = get_object_or_404(Commentaires, pk=id)

    if request.method == "POST":
        form = CommentairesForm(
            request.POST or None,
            request.FILES or None,
            instance=commentaire
        )

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/commentaires/")
    else:
        form = CommentairesForm(instance=commentaire)

    return render(request, "seefilm/commentaireupdate.html", {
        "form": form,
        "commentaire": commentaire
    })

def updateFilms(request, id):
    film = get_object_or_404(Films, pk=id)

    if request.method == "POST":
        form = FilmsForm(
            request.POST or None,
            request.FILES or None,
            instance=film
        )

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/films/")
    else:
        form = FilmsForm(instance=film)

    return render(request, "seefilm/filmupdate.html", {
        "form": form,
        "film": film
    })

def updateCategories(request, id):
    categorie = get_object_or_404(Categories, pk=id)

    if request.method == "POST":
        form = CategoriesForm(
            request.POST or None,
            request.FILES or None,
            instance=categorie
        )
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/categories/")
    else:
        form = CategoriesForm(instance=categorie)

    return render(request, "seefilm/catupdate.html", {
        "form": form,
        "categorie": categorie
    })
def updateActeurs(request, id):
    acteur = get_object_or_404(Acteurs, pk=id)

    if request.method == "POST":
        form = ActeursForm(
            request.POST or None,
            request.FILES or None,
            instance=acteur
        )

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/acteurs/")

    else:
        form = ActeursForm(instance=acteur)

    return render(
        request,
        "seefilm/acteurupdate.html",
        {
            "form": form,
            "acteur": acteur
        }
    )

#DELETE
def deleteCommentaires(request, id):
    commentaire = get_object_or_404(Commentaires, pk=id)
    commentaire.delete()
    return HttpResponseRedirect("/commentaires/")


def deleteFilms(request, id):
    film = get_object_or_404(Films, pk=id)
    film.delete()
    return HttpResponseRedirect("/films/")

def deleteCategories(request, id):
    categorie = get_object_or_404(Categories, pk=id)
    categorie.delete()
    return HttpResponseRedirect("/categories/")

def deleteActeurs(request, id):
    acteur = get_object_or_404(Acteurs, pk=id)

    acteur.delete()

    return HttpResponseRedirect("/acteurs/")

#TRAITEMENT AJOUT
def traitementCategories(request):
    cform = CategoriesForm(request.POST)

    if cform.is_valid():
        categorie = cform.save()

        return render(
            request,
            "seefilm/cataffiche.html",
            {"categorie": categorie}
        )

    else:
        return render(
            request,
            "seefilm/catajout.html",
            {"form": cform}
        )

def traitementActeurs(request):
    aform = ActeursForm(request.POST)

    if aform.is_valid():

        acteur = aform.save()

        return render(
            request,
            "seefilm/acteuraffiche.html",
            {"acteur": acteur}
        )

    else:

        return render(
            request,
            "seefilm/acteurajout.html",
            {"form": aform}
        )
def updatetraitementCategories(request, id):

    if request.method == 'POST':

        cform = CategoriesForm(request.POST)

        if cform.is_valid():

            categorie = cform.save(commit=False)
            categorie.id = id
            categorie.save()

            return HttpResponseRedirect("/categories/")

        else:

            categorie = Categories.objects.get(pk=id)

            return render(
                request,
                "seefilm/catupdate.html",
                {
                    "categorie": categorie,
                    "form": cform
                }
            )

def updatetraitementActeurs(request, id):

    if request.method == "POST":

        aform = ActeursForm(request.POST)

        if aform.is_valid():

            acteur = aform.save(commit=False)
            acteur.id = id
            acteur.save()

            return HttpResponseRedirect("/acteurs/")

        else:

            acteur = Acteurs.objects.get(pk=id)

            return render(
                request,
                "seefilm/acteurupdate.html",
                {
                    "acteur": acteur,
                    "form": aform
                }
            )

