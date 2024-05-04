from django.db import models
from django.contrib.auth.models import  User

# Create your models here.


class Recipes(models.Model):
    user=  models.ForeignKey(User, on_delete=models.SET_NULL, null=True , blank=True)
    recipe_name= models.TextField(max_length=100)
    description= models.TextField()
    image= models.ImageField(upload_to="images")

    
