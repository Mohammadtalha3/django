from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    
    peoples= [
        {'name':'Talalhussain', 'age':32},
        {'name':'Sanadhussain', 'age':26},
        {'name':'MuhammadTalha', 'age':24} 
    ]
    
    return render(request, 'index.html', context={'page': "learning django", 'peoples':peoples})

def about (request):
    context= {'page':'About'}
    return render( request, 'about.html', context)

def contact(request):
    context= {'page':'Contact'}
    return render(request, 'contact.html', context)
