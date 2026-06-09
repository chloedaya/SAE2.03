from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .forms import CategoriesForm
from .models import Categories

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
            acteurs = form.save()
            return render(request, "seefilm/acteuraffiche.html", {
                "acteur": acteur
            })
    else:
        form = ActeursForm()

    return render(request, "seefilm/acteurajout.html", {
        "form": form
    })


def allCategories(request):
    liste_categorie = Categories.objects.all()

    return render(request, "seefilm/categories.html", {
        "liste_categorie": liste_categorie
    })


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


def deleteCategories(request, id):
    categorie = get_object_or_404(Categories, pk=id)
    categorie.delete()
    return HttpResponseRedirect("/categories/")

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