from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages
from  django.db.models import Q
from .models import *
from django.contrib.auth import get_user_model


User= get_user_model()

# Create your views here.

@login_required(login_url='/login/')
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

def logout_page(request):
    logout(request)
    return redirect('/login/')

def login_page(request):

    if request.method== "POST":
        username= request.POST.get('username')
        password= request.POST.get('password')

        print('we got this username from login', username)
        print('we got this password from login:', password)

        if not User.objects.filter(username=username).exists():
            
            
        

            messages.error(request, 'Invalid Username Please make sure you have account registered by this name ')
            return redirect('/register')


        
        
        user= authenticate(username= username,  password= password)

        if user is None:
            messages.error(request, "Invalid credentials ")
            print("we are redirecting user is none: ")
            return redirect('/login')
        else:
            login(request, user)
            return redirect('/recipes')

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

def get_students(request):
    queryset= student.objects.all()

    if request.GET.get('search'):

        search= request.GET.get('search')

        queryset= queryset.filter(
            Q(student_name__icontains= search) |
            Q(department__department__icontains= search)
            
            )

    paginator = Paginator(queryset, 10)  

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    

    return render(request,'students.html', {'queryset':page_obj})

def report_card(request):
   
   subjects= sunjectmarks.objects.all()
   students= student.objects.all()

   stduent_data=[]

   for std in students:
       
       student_subject= sunjectmarks.objects.filter(student=std)
       subject_marks= [ sub.subject.subject_name   for sub in student_subject]
       #sub_marks= ''.join(subject_marks)
       marks= [sun.marks  for sun in student_subject]
      
       
       total_marks= [sub.student.Total_marks  for sub in student_subject]
       
       

       stduent_data.append({
           'student_name':std.student_name,
           'Department': std.department.department,
           'subjects': subject_marks,
           'maeks': marks,
           'total_marks': total_marks[0]

       })

       for i in stduent_data:
           print(i)

       context= {
           "Student_data" :stduent_data,
           'subjects': subjects
       }

       
       
   return render(request, 'reportcard.html', context)



