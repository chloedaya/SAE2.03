from django.urls import path,include
from . import views

urlpatterns = [
    path('films/', views.seefilms, name='seefilms'),
    path('acteurs/', views.seeacteurs, name='seeacteurs'),
    path('categories/', views.seecategories, name='seecategories'),
    path('personnes/', views.seepersonnes, name='seepersonnes'),
    path('commentaires/', views.seecommentaires, name='seecommentaires'),
]