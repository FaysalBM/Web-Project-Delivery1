from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from .forms import CreateUserForm

@csrf_exempt
def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form':form}

    return render(request, 'registration/register.html', context) 

def home(request):
    return render(request, 'web/home.html')

def about(request):
    return render(request, 'web/about.html', {'title': 'About Us'})

def create_project(request):
    return render(request, 'web/create_project.html', {'title': 'Create Project'})