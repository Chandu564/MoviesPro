from django.db import models
class Movie(models.Model):
    title=models.CharField(max_length=100)
    language=models.CharField(max_length=20)
    poster=models.ImageField(upload_to='pics')
    release_year=models.IntegerField()
    lead_actor=models.CharField(max_length=200)
    rating=models.FloatField()
# Create your models here.
