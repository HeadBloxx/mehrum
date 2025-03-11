from django.db import models

# Create your models here.
class Mehrum(models.Model):
    ime = models.CharField(max_length=40)
    slika = models.ImageField(upload_to=r"%Y/%m/%d")
    datum = models.DateTimeField(auto_now_add=True)