from django.db import models

# Create your models here.


class Recipes(models.Model):
    recipe_name= models.TextField(max_length=100)
    description= models.TextField()
    image= models.ImageField(upload_to="images")

    
