from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models


class CategoriesForm(ModelForm):
    class Meta:
        model = models.Categories
        fields = ('nom', 'descriptif')

        labels = {
            'nom': _('Nom'),
            'descriptif': _('Descriptif')
        }


class ActeursForm(ModelForm):
    class Meta:
        model = models.Acteurs
        fields = ('nom', 'prenom', 'age', 'photo')

        labels = {
            'nom': _('Nom'),
            'prenom': _('Prénom'),
            'age': _('Age'),
            'photo': _('Photo')
        }


class FilmForm(ModelForm):
    class Meta:
        model = models.Film
        fields = (
            'titre',
            'annee_sortie',
            'affiche',
            'realisateur',
            'categorie',
            'acteurs'
        )

        labels = {
            'titre': _('Titre'),
            'annee_sortie': _('Année de sortie'),
            'affiche': _('Affiche'),
            'realisateur': _('Réalisateur'),
            'categorie': _('Catégorie'),
            'acteurs': _('Acteurs')
        }


class PersonnesForm(ModelForm):
    class Meta:
        model = models.Personnes
        fields = (
            'pseudo',
            'nom',
            'prenom',
            'mail',
            'mot_de_passe',
            'type_personne'
        )

        labels = {
            'pseudo': _('Pseudo'),
            'nom': _('Nom'),
            'prenom': _('Prénom'),
            'mail': _('Mail'),
            'mot_de_passe': _('Mot de passe'),
            'type_personne': _('Type')
        }


class CommentairesForm(ModelForm):
    class Meta:
        model = models.Commentaires
        fields = (
            'film',
            'personne',
            'note',
            'commentaire'
        )

        labels = {
            'film': _('Film'),
            'personne': _('Personne'),
            'note': _('Note'),
            'commentaire': _('Commentaire')
        }