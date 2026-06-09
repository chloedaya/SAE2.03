from django.urls import path,include
from . import views

urlpatterns = [
    path('/catajout/', views.ajoutCategories),
    path('catall/', views.allCategories),
    path('traitementCategorie/', views.traitementCategories),
    path('categories/', views.allCategories),
    path('cataffiche/<int:id>/', views.readCategories),
    path('update/<int:id>/', views.updateCategories),
    path('updatetraitement/<int:id>/', views.updatetraitementCategories),
    path('', views.allCategories),
    path('read/<int:id>/', views.readCategories),
    path('delete/<int:id>/', views.deleteCategories),

]