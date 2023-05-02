from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from wpApp.form import ProjectForm
@login_required
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
            form.save_m2m()
            return redirect('project_detail', pk=project.pk)
    else:
        form = ProjectForm()
    return render(request, 'web/create_project.html', {'form': form})

def home(request):
    return render(request, 'web/home.html')

def about(request):
    return render(request, 'web/about.html', {'title': 'About Us'})

def create_project(request):
    return render(request, 'web/create_project.html', {'title': 'Create Project'})