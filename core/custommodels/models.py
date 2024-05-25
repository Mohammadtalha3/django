from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManger

# Create your models here.


class custommodel(AbstractUser):

    username= None
    phone_number= models.CharField(max_length=15, unique=True)
    email= models.EmailField(unique=True)
    user_bio= models.CharField(max_length=100)
    profile= models.ImageField(upload_to='profile')

    
    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS=[]
    objects= UserManger()

