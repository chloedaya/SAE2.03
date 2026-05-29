from django.db import models

# Create your models here.
class Seefilm(models.model):
    Username=models.CharField(max_length=100)
    Film vu=models.CharField(max_length=100)