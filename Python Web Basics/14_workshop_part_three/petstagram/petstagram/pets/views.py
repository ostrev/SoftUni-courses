from django.shortcuts import render, redirect

from petstagram.pets.forms import PetCreateForm, PetEditForm
from petstagram.pets.models import Pet


# Create your views here.


def pet_details(request, username, pet_name):
    pet = Pet.objects.get(slug=pet_name)
    all_photos = pet.photo_set.all()

    context = {
        'pet': pet,
        'all_photos': all_photos,
    }
    return render(request, 'pets/pet-details-page.html', context)


def pet_add(request):
    if request.method == 'GET':
        form = PetCreateForm()
    else:
        form = PetCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile details', pk=1)  # TODO fix this when auth

    context = {
        'form': PetCreateForm()
    }
    return render(request, 'pets/pet-add-page.html', context)


def pet_edit(request, username, pet_name):
    # TODO use username when auth
    instance = Pet.objects.filter(slug=pet_name).get()
    if request.method == 'GET':
        form = PetEditForm(instance=instance)
    else:
        form = PetEditForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('pet details', username=username, pet_name=pet_name)

    context = {
        'form': form,
        'username': username,
        'pet_slug': pet_name,
    }

    return render(request, 'pets/pet-edit-page.html', context)


def pet_delete(request, username, pet_name):
    return render(request, 'pets/pet-delete-page.html')
