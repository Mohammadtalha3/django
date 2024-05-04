from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
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

    if request.GET.get('search'):
        queryset= queryset.filter(recipe_name__icontains=request.GET.get('search'))
    context= {'recipes':queryset}
    return  render(request, 'recipes.html', context)


def delete(request,id):

    queryset= Recipes.objects.get(id=id)
    queryset.delete()

    return redirect('/recipes/')

def update(request,id):
    
    queryset= Recipes.objects.get(id=id)

    if request.method=='POST':
        data= request.POST
        recipe_Image= request.FILES.get('image')
        recipe_name= data.get('recipe_name')
        description= data.get('description')

        queryset.recipe_name= recipe_name
        queryset.description= description
        if recipe_Image:
            queryset.image= recipe_Image
        
        queryset.save()
        return redirect('/recipes')

    context= {'recipe': queryset}
    

    return render(request, 'update_recipe.html', context)

def login_page(request):
    return render(request, 'login.html')

def register(request):
    if request.method=='POST':
        first_name= request.POST.get('firstname')
        last_name= request.POST.get('lastname')
        username= request.POST.get('username')
        password=request.POST.get('password')


        user= User.objects.filter(username= username)

        if user.exists():
            messages.info(request, 'Username already taken')
            return redirect('/register')

        user= User.objects.create(
            first_name= first_name,
            last_name= last_name,
            username= username,

        )
        user.set_password(password)
        user.save()
        messages.info(request, 'Account created Successfully')

        return redirect('/register')


    return render(request, 'register.html')
