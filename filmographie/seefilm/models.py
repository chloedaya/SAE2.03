from django.db import models

# Create your models here.

class Categories(models.Model):
    idcategories = models.AutoField(primary_key=True)
    nomCat = models.CharField(max_length=100)
    descriptif = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'categories'
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.nomCat

class Acteurs(models.Model):
    idacteurs = models.AutoField(primary_key=True)
    nomAct = models.CharField(max_length=45)
    prenomAct = models.CharField(max_length=45)
    age = models.IntegerField(blank=True, null=True)
    photo = models.ImageField(
        upload_to='acteurs/',
        blank=True,
        null=True,
        editable=True,
    )

    class Meta:
        db_table = 'acteurs'
        verbose_name_plural = "Acteurs"

    def __str__(self):
        return f"{self.prenomAct} {self.nomAct}"

class Personnes(models.Model):
    idpersonnes = models.AutoField(primary_key=True)
    pseudo = models.CharField(max_length=45, unique=True)
    nomPer = models.CharField(max_length=45)
    prenomPer = models.CharField(max_length=45)
    mail = models.EmailField(max_length=100, unique=True)
    mot_de_passe = models.CharField(max_length=25)

    type = models.CharField(
        max_length=15,
        choices=[
            ('professionnel', 'Professionnel'),
            ('amateur', 'Amateur'),
        ]
    )

    class Meta:
        db_table = 'personnes'
        verbose_name_plural = "Personnes"

    def __str__(self):
        return self.pseudo


class Films(models.Model):
    idfilms = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=45)
    anneesortie = models.IntegerField()  # year
    affiche = models.ImageField(
        editable=True,
        upload_to='affiches/'

    )
    realisateur = models.CharField(max_length=45)
    idcategorie = models.ForeignKey(Categories,on_delete=models.SET_NULL,null=True,blank=True,db_column='idcategorie')
    acteurs = models.CharField(max_length=45)

    class Meta:
        db_table = 'films'
        verbose_name_plural = "Films"

    def __str__(self):
        return self.titre

class FilmsActeurs(models.Model):
    idfilms = models.ForeignKey(Films, on_delete=models.PROTECT, db_column='idfilms')
    idacteurs = models.ForeignKey(Acteurs, on_delete=models.PROTECT, db_column='idacteurs')

    class Meta:
        db_table = 'films_acteurs'
        unique_together = (('idfilms', 'idacteurs'),)
        verbose_name_plural = "Films Acteurs"

class Commentaires(models.Model):
    idcommentaires = models.AutoField(primary_key=True)
    note = models.IntegerField()
    commentaire = models.TextField()
    dateCom = models.DateTimeField()

    idfilmsC = models.ForeignKey(
        Films,
        on_delete=models.SET_NULL,
        null=True,
        db_column='idfilmsC'
    )
    idpersonnesC = models.ForeignKey(
        Personnes,
        on_delete=models.SET_NULL,
        null=True,
        db_column='idpersonnesC'
    )

    class Meta:
        db_table = 'commentaires'
        verbose_name_plural = "Commentaires"