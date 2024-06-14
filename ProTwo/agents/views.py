from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm, AddLocationForm, AddPropertyForm, UserProfileForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate 
from AppTwo.models import *
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required


# Create your views here.


def register(request):
    if request.method == 'POST':
        reg = RegistrationForm(request.POST)
        if reg.is_valid():
            reg.save()
            messages.success(request, 'User Registered')
            return redirect('agents:user_login')
    else:
        reg = RegistrationForm()
    context = {'reg': reg}
    return render(request, 'agents/register.html', context)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('agents:user_dashboard')
        else:
            messages.error(request, 'Incorrect Username or Password')
    context = {}
    return render(request, 'agents/login.html', context)

@login_required(login_url='/agent/login/')
def user_dashboard(request):
    agent_profile = User.objects.get(username=request.user)
    property = Property.objects.filter(agent__user=agent_profile).order_by('-created_at')  
    context={
        'property':property,
    }
    return render(request, 'agents/dashboard.html', context)

@login_required(login_url='/agent/login/')
def add_location(request):
    if request.method == 'POST':
        location = AddLocationForm(request.POST)
        if location.is_valid():
            new_location = location.save(commit=False)
            new_location.slug = slugify(new_location.name)
            new_location.save()
            messages.success(request, 'Location Added')
    else:
        location = AddLocationForm()
    context={
        'location': location,
    }
    return render(request, 'agents/add-location.html', context)

@login_required(login_url='/agent/login/')
def add_property(request):
    if request.method == 'POST':
        property = AddPropertyForm(request.POST, request.FILES)
        if property.is_valid():
            agent_profile = request.user.userprofile
            new_property = property.save(commit=False)
            new_property.agent = agent_profile
            new_property.save()
            messages.success(request, 'Property Added')
    else:
        property = AddPropertyForm()
    context = {
        'property':property
    }
    return render(request, 'agents/add-property.html', context)

@login_required(login_url='/agent/login/')
def user_logout(request):
    logout(request)
    return redirect('agents:user_login')

@login_required(login_url='/agent/login/')
def user_profile(request):
    if request.method == 'POST':
        profile = UserProfileForm(request.POST, request.FILES)
        if profile.is_valid():
            new_profile = profile.save(commit=False)
            new_profile.user = request.user
            new_profile.save()
            return redirect('agents:user_dashboard')
    else:
        profile = UserProfileForm()
    context = {
        'profile':profile
    }
    return render(request, 'agents/user-profile.html', context)

@login_required(login_url='/agent/login/')
def delete_property(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    property.delete()
    return redirect('agents:user_dashboard')

@login_required(login_url='/agent/login/')
def edit_property(request, property_id):
    get_single_prop = Property.objects.get(id=property_id)
    if request.method == 'POST':
        edit_prop = AddPropertyForm(request.POST, request.FILES, instance=get_single_prop)
        if edit_prop.is_valid:
            edit_prop.save()
            return redirect('agents:user_dashboard')
    else:
        edit_prop=AddPropertyForm(instance=get_single_prop)
    return render(request, 'agents/edit-property.html', {'edit':edit_prop})