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
]