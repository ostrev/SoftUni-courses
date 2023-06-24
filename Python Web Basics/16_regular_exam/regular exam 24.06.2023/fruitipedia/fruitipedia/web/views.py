from django.shortcuts import render, redirect

from fruitipedia.web.forms import CreateProfileForm, CreateFruitForm, EditFruitForm, DeleteFruitForm, EditProfileForm, \
    DeleteProfileForm
from fruitipedia.web.models import Profile, Fruit


def get_profile():
    profile = Profile.objects.first()
    return profile


def index(request):
    profile = get_profile()

    context = {
        'profile': profile,
    }
    return render(request, 'web/index.html', context)


def dashboard(request):
    profile = get_profile()

    if not profile:
        return redirect('home')
    fruits = Fruit.objects.all()

    context = {
        'profile': profile,
        'fruits': fruits

    }
    return render(request, 'web/dashboard.html', context)


def create_fruit(request):
    profile = get_profile()

    if not profile:
        return redirect('home')
    if request.method == 'GET':
        form = CreateFruitForm()
    else:
        form = CreateFruitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'web/create-fruit.html', context)


def details_fruit(request, pk):
    profile = get_profile()

    if not profile:
        return redirect('home')
    fruit = Fruit.objects.filter(pk=pk).get()

    context = {
        'profile': profile,
        'fruit': fruit,
    }
    return render(request, 'web/details-fruit.html', context)


def edit_fruit(request, pk):
    profile = get_profile()

    if not profile:
        return redirect('home')
    fruit = Fruit.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = EditFruitForm(instance=fruit)
    else:
        form = EditFruitForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {
        'profile': profile,
        'form': form,
        'fruit': fruit,
    }
    return render(request, 'web/edit-fruit.html', context)


def delete_fruit(request, pk):
    profile = get_profile()

    if not profile:
        return redirect('home')

    fruit = Fruit.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = DeleteFruitForm(instance=fruit)
    else:
        form = DeleteFruitForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {
        'profile': profile,
        'form': form,
        'fruit': fruit
    }
    return render(request, 'web/delete-fruit.html', context)


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
            return redirect('dashboard')

    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'web/create-profile.html', context)


def details_profile(request):
    profile = get_profile()

    if not profile:
        return redirect('home')
    number_of_fruits = Fruit.objects.all().count()
    context = {
        'profile': profile,
        'number_of_fruits': number_of_fruits,

    }
    return render(request, 'web/details-profile.html', context)


def edit_profile(request):
    profile = get_profile()

    if not profile:
        return redirect('home')
    if request.method == 'GET':
        form = EditProfileForm(instance=profile)
    else:
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details profile')
    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'web/edit-profile.html', context)


def delete_profile(request):
    profile = get_profile()

    if not profile:
        return redirect('home')
    if request.method == 'GET':
        form = DeleteProfileForm(instance=profile)
    else:
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            Fruit.objects.all().delete()
            return redirect('home')
    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'web/delete-profile.html', context)
