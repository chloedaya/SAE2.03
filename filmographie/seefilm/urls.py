from django.urls import path,include
from . import views


urlpatterns = [
    path('catajout/', views.ajoutCategories, name='catajout'),
    path('traitementCategorie/', views.traitementCategories, name='traitementCategorie'),

    path('categories/', views.allCategories, name='categories'),

    path('cataffiche/<int:id>/', views.readCategories, name='cataffiche'),
    path('update/<int:id>/', views.updateCategories, name='updateCategorie'),
    path('updatetraitement/<int:id>/', views.updatetraitementCategories),

    path('delete/<int:id>/', views.deleteCategories, name='deleteCategorie'),

    path('', views.allCategories),


    # ACTEURS

    path('acteurajout/', views.ajoutActeurs, name='acteurajout'),
    path('traitementActeur/', views.traitementActeurs, name='traitementActeur'),

    path('acteurs/', views.allActeurs, name='acteurs'),

    path('acteuraffiche/<int:id>/', views.allActeurs, name='acteuraffiche'),
    path('acteurupdate/<int:id>/', views.updateActeurs, name='updateActeur'),
    path('acteurupdatetraitement/<int:id>/', views.updatetraitementActeurs),

    path('acteurdelete/<int:id>/', views.deleteActeurs, name='deleteActeur'),
]


