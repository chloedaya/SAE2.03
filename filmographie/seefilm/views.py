from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import CategoriesForm
from . import models
from .models import Categories


def ajoutCategories(request):
    if request.method == "POST":
        form = CategoriesForm(request.POST)

        if form.is_valid():
            categories = form.save()
            return render(
                request,
                "seefilm/cataffiche.html",
                {"categorie": categorie}
            )
        else:
            return render(
                request,
                "seefilm/catajout.html",
                {"form": form}
            )

    else:
        form = CategoriesForm()
        return render(
            request,
            "seefilm/catajout.html",
            {"form": form}
        )


def traitementCategorie(request):
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


def allCategories(request):
    liste_categorie = list(models.Categories.objects.all())

    return render(
        request,
        "seefilm/allCategorie.html",
        {"liste_categorie": liste_categorie}
    )


def readCategories(request, id):
    categorie = models.Categorie.objects.get(pk=id)

    return render(
        request,
        "seefilm/cataffiche.html",
        {"categorie": categorie}
    )


def updateCategorie(request, id):
    categorie = models.Categories.objects.get(pk=id)

    cform = CategoriesForm(categorie.__dict__)

    return render(
        request,
        "seefilm/catupdate.html",
        {
            "categorie": categorie,
            "form": cform
        }
    )


def updatetraitementCategorie(request, id):

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


def deleteCategorie(request, id):
    categorie = Categories.objects.get(pk=id)

    categorie.delete()

    return HttpResponseRedirect("/categories/")