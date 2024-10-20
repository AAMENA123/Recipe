from django.shortcuts import render, redirect
from vege.models import *


def recipes(request):
    if request.method =="POST":
            data = request.POST
            a = data.get('recipe_name')
            b = data.get('recipe_description')
            c = request.FILES.get('recipe_image')
            print(a,b,c)
            Recipe.objects.create(recipe_name = a,recipe_description = b, recipe_image = c)
            return redirect('/recipe/')
    return render(request,'recipes.html')
   
def home(request):
    recipe = Recipe.objects.all()
    if request.GET.get('search_recipe'):
        recipes = Recipe.objects.filter(recipe_name__icontains =request.GET.get('search_recipe') )
        return render(request, 'home.html', {'recipes': recipes     })
    if request.POST.get('some'):
        return redirect('/home/')
    return render(request, 'home.html', {'recipes': recipe})

def delete_recipe(request, id):
    queryset = Recipe.objects.get(id = id)
    queryset.delete()
    return redirect('/home/')

def update_recipe(request, id):
    recipes = Recipe.objects.get(id = id)
    print(id)
    if request.method =="POST":
        recipes.recipe_name = request.POST.get('recipe_name')
        recipes.recipe_description =request.POST.get('recipe_description')
        if request.FILES.get('recipe_image'):
          recipes.recipe_image =request.FILES.get('recipe_image')
        recipes.save()
        return redirect('/update/')
    return render(request, "update_recipe.html",{'recipes': recipes})

def update_recipe1(request):
    return render(request, "update_recipe.html")

def login(request):
    return render(request, "login.html")

def register(request):
    if request.method =="POST":
        first_name = 
    return render(request, "register.html")