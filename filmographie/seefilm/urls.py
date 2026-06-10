from django.urls import path,include
from . import views



urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('catajout/', views.ajoutCategories, name='catajout'),
    path('traitementCategorie/', views.traitementCategories, name='traitementCategorie'),

    path('categories/', views.allCategories, name='seecategories'),

    path('cataffiche/<int:id>/', views.readCategories, name='cataffiche'),
    path('update/<int:id>/', views.updateCategories, name='updateCategorie'),
    path('updatetraitement/<int:id>/', views.updatetraitementCategories),

    path('delete/<int:id>/', views.deleteCategories, name='deleteCategorie'),

    path('', views.allCategories),


    # ACTEURS

    path('acteurajout/', views.ajoutActeurs, name='acteurajout'),
    path('traitementActeur/', views.traitementActeurs, name='traitementActeur'),

    path('acteurs/', views.allActeurs, name='seeacteurs'),

    path('acteuraffiche/<int:id>/', views.allActeurs, name='acteuraffiche'),
    path('acteurupdate/<int:id>/', views.updateActeurs, name='updateActeur'),
    path('acteurupdatetraitement/<int:id>/', views.updatetraitementActeurs),

    path('acteurdelete/<int:id>/', views.deleteActeurs, name='deleteActeur'),

    path('films/', views.allFilms, name='seefilms'),
    path('filmajout/', views.ajoutFilms, name='filmajout'),
    path('filmaffiche/<int:id>/', views.readFilms, name='filmaffiche'),
    path('filmupdate/<int:id>/', views.updateFilms, name='filmupdate'),
    path('filmdelete/<int:id>/', views.deleteFilms),

    path('commentaires/', views.allCommentaires, name='seecommentaires'),
    path('commentaireajout/', views.ajoutCommentaires, name='commentaireajout'),
    path('commentaireaffiche/<int:id>/', views.readCommentaires, name='commentaireaffiche'),
    path('commentaireupdate/<int:id>/', views.updateCommentaires, name='commentaireupdate'),
    path('commentairedelete/<int:id>/', views.deleteCommentaires),




]


