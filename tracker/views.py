from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import JobForm, CustomAuthForm, CustomUserCreationForm
from .models import Job
from datetime import date

# Home page
@login_required
def home(request):
    jobs = Job.objects.filter(user=request.user)
    today = date.today()
    return render(request, 'home.html', {'jobs': jobs, 'today': today})

# Login
def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
        messages.error(request, "Invalid username or password")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Register
def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully! You can now log in.")
            return redirect('login')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
     

# Add job
@login_required
def add_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.user = request.user
            job.save()
            return redirect('home')
    else:
        form = JobForm()
    return render(request, 'add_job.html', {'form': form})

# edit_job
@login_required
def edit_job(request, job_id):
    job = Job.objects.get(id=job_id, user=request.user)
    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = JobForm(instance=job)
    return render(request, 'edit_job.html', {'form': form})

# delete_job
def delete_job(request, job_id):
    job = get_object_or_404(Job, id=job_id, user=request.user)
    if request.method == 'POST':
        job.delete()
        return redirect('home')
    return render(request, 'delete_job.html', {'job': job})


# Logout
def logout_user(request):
    logout(request)
    messages.info(request, "Logged out successfully.")
    return redirect('login')



