from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models


class CategoriesForm(ModelForm):
    class Meta:
        model = models.Categories
        fields = ('nomCat', 'descriptif')

        labels = {
            'nomCat': _('Nom'),
            'descriptif': _('Descriptif')
        }


class ActeursForm(ModelForm):
    class Meta:
        model = models.Acteurs
        fields = ('nomAct', 'prenomAct', 'age', 'photo')

        labels = {
            'nomAct': _('Nom'),
            'prenomAct': _('Prénom'),
            'age': _('Âge'),
            'photo': _('Photo')
        }


class FilmForm(ModelForm):
    class Meta:
        model = models.Films
        fields = (
            'titre',
            'anneesortie',
            'affiche',
            'realisateur',
            'idcategorie',
            'acteurs'
        )

        labels = {
            'titre': _('Titre'),
            'anneesortie': _('Année de sortie'),
            'affiche': _('Affiche'),
            'realisateur': _('Réalisateur'),
            'idcategorie': _('Catégorie'),
            'acteurs': _('Acteurs')
        }


class PersonnesForm(ModelForm):
    class Meta:
        model = models.Personnes
        fields = (
            'pseudo',
            'nomPer',
            'prenomPer',
            'mail',
            'mot_de_passe',
            'type'
        )

        labels = {
            'pseudo': _('Pseudo'),
            'nomPer': _('Nom'),
            'prenomPer': _('Prénom'),
            'mail': _('Mail'),
            'mot_de_passe': _('Mot de passe'),
            'type': _('Type')
        }


class CommentairesForm(ModelForm):
    class Meta:
        model = models.Commentaires
        fields = (
            'idfilmsC',
            'idpersonnesC',
            'note',
            'commentaire',
            'dateCom'
        )

        labels = {
            'idfilmsC': _('Film'),
            'idpersonnesC': _('Personne'),
            'note': _('Note'),
            'commentaire': _('Commentaire'),
            'dateCom': _('Date')
        }