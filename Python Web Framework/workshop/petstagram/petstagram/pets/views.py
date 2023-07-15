from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from petstagram.accounts.models import PetstagramUser
from petstagram.pets.forms import PetCreateForm, PetEditForm, PetDeleteForm
from petstagram.pets.models import Pet


UserModel = get_user_model()


@login_required
def pet_details(request, username, pet_name):
    pet = Pet.objects.get(slug=pet_name)
    owner = PetstagramUser.objects.get(username=username)
    all_photos = pet.photo_set.all()

    context = {
        'pet': pet,
        'all_photos': all_photos,

        'owner': owner,
    }
    return render(request, 'pets/pet-details-page.html', context)


@login_required
def pet_add(request):
    if request.method == 'GET':
        form = PetCreateForm()
    else:
        form = PetCreateForm(request.POST)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.user = request.user
            pet.save()

            return redirect('profile details', pk=request.user.pk)

    context = {
        'form': form
    }
    return render(request, 'pets/pet-add-page.html', context)


@login_required
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
        'pet_name': pet_name,
    }

    return render(request, 'pets/pet-edit-page.html', context)


@login_required
def pet_delete(request, username, pet_name):
    instance = Pet.objects.filter(slug=pet_name).get()
    if request.method == 'GET':
        form = PetDeleteForm(instance=instance)
    else:
        form = PetDeleteForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('profile details', pk=1)
    context = {
        'form': form,
        'username': username,
        'pet_name': pet_name,
    }
    return render(request, 'pets/pet-delete-page.html', context)
