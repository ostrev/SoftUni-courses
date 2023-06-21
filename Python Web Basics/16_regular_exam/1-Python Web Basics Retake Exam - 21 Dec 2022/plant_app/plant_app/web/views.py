from django.shortcuts import render, redirect

from plant_app.web.forms import CreateProfileForm, CreatePlantForm, EditPlantForm, DeletePlantForm, EditProfileForm, \
    DeleteProfileForm
from plant_app.web.models import Profile, Plant


def get_profile():
    profile = Profile.objects.first()
    return profile


def get_plants():
    plants = Plant.objects.all()
    return plants


# Create your views here.
def index(request):
    profile = get_profile()

    context = {
        'profile': profile
    }
    return render(request, 'web/home-page.html', context)


def catalogue(request):
    profile = get_profile()
    plants = get_plants()
    context = {
        'profile': profile,
        'plants': plants,
    }

    return render(request, 'web/catalogue.html', context)


def create_plant(request):
    profile = get_profile()
    if request.method == 'GET':
        form = CreatePlantForm()
    else:
        form = CreatePlantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'profile': profile
    }

    return render(request, 'web/create-plant.html', context)


def details_plant(request, pk):
    profile = get_profile()
    plant = Plant.objects.filter(pk=pk).get()
    context = {
        'plant': plant,
        'profile': profile
    }
    return render(request, 'web/plant-details.html', context)


def edit_plant(request, pk):
    profile = get_profile()
    plant = Plant.objects.filter(pk=pk).get()
    if request.method == "GET":
        form = EditPlantForm(instance=plant)
    else:
        form = EditPlantForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {
        'profile': profile,
        'plant': plant,
        'form': form,
    }

    return render(request, 'web/edit-plant.html', context)


def delete_plant(request, pk):
    profile = get_profile()
    plant = Plant.objects.filter(pk=pk).get()
    if request.method == "GET":
        form = DeletePlantForm(instance=plant)
    else:
        form = DeletePlantForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {
        'profile': profile,
        'plant': plant,
        'form': form,
    }

    return render(request, 'web/delete-plant.html', context)


def create_profile(request):
    profile = get_profile()
    if profile:
        return redirect('home')
    if request.method == 'GET':
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form
    }

    return render(request, 'web/create-profile.html', context)


def details_profile(request):
    profile = get_profile()
    stars = Plant.objects.all().count()

    context = {
        'profile': profile,
        'stars': stars,
    }

    return render(request, 'web/profile-details.html', context)


def edit_profile(request):
    profile = get_profile()
    if request.method == "GET":
        form = EditProfileForm(instance=profile)
    else:
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details profile')

    context = {
        'profile': profile,
        'form': form
    }

    return render(request, 'web/edit-profile.html', context)


def delete_profile(request):
    profile = get_profile()
    if request.method == "GET":
        form = DeleteProfileForm(instance=profile)
    else:
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            Plant.objects.all().delete()
            return redirect('home')

    context = {
        'profile': profile,
        'form': form
    }

    return render(request, 'web/delete-profile.html', context)
