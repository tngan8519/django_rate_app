from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.
class Individual(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    image = models.ImageField()
    description = models.CharField(max_length=400)
    created = models.DateTimeField(auto_now_add=True)
    
class Rating(models.Model):
    individual = models.ForeignKey(Individual, on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    rating = models.IntegerField()
    text = models.CharField(max_length=400)
    created = models.DateTimeField(auto_now_add=True)



