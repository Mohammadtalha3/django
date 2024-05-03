from django.shortcuts import render, redirect
from .models import *

# Create your views here.


def Recipes_func(request):
    if request.method =='POST':

        data=request.POST
        print(data)
        recipe_Image= request.FILES.get('image')
        recipe_name= data.get('recipe_name')
        description= data.get('description')
        
        Recipes.objects.create(recipe_name=recipe_name,description=description,image=recipe_Image)

        return redirect('/recipes/')

    queryset= Recipes.objects.all()
    context= {'recipes':queryset}
    return  render(request, 'recipes.html', context)


def delete(request,id):

    queryset= Recipes.objects.get(id=id)
    queryset.delete()

    return redirect('/recipes/')
