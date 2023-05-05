from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from .models import Company, Department
@csrf_exempt
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account was created for ' + form.cleaned_data.get('username'))
            return redirect('login_user')
    context = {'form':form}

    return render(request, 'registration/register.html', context) 

@csrf_exempt
def loginPage(request):
    """if request.user.is_authenticated:
        return redirect('web-home')
    else:"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            #return redirect('web-home')
            return redirect('web-home')
        else:
            messages.info(request, 'Username OR password is incorrect')
    context = {}
    return render(request, 'registration/login.html', context)

def company_detail(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    return render(request, 'models/company_detail.html', {'company': company})

def department_detail(request, department_id):
    department = get_object_or_404(Department, pk=department_id)
    return render(request, 'models/department_detail.html', {'department': department})

def logoutPage(request):
    logout(request)
    return redirect('login_user')

@login_required(login_url='login')
def home(request):
    companies = Company.objects.filter(workers=request.user)
    return render(request, 'web/home.html',  {'companies': companies}) #

@login_required(login_url='login')
def about(request):
    return render(request, 'web/about.html', {'title': 'About Us'})

@login_required(login_url='login')
def create_project(request):
    
    return render(request, 'web/create_project.html', {'title': 'Create Project'})