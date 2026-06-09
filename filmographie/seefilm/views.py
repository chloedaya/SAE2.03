from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .forms import CategoriesForm, ActeursForm
from .models import Categories, Acteurs

#LES AJOUTS
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
        form = ActeursForm(request.POST)

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

#LES ALL
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

def readCategories(request, id):
    categorie = get_object_or_404(Categories, pk=id)

    return render(request, "seefilm/cataffiche.html", {
        "categorie": categorie
    })


def updateCategories(request, id):
    categorie = get_object_or_404(Categories, pk=id)

    if request.method == "POST":
        form = CategoriesForm(request.POST, instance=categorie)
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
            request.POST,
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