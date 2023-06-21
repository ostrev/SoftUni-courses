from django.shortcuts import render, redirect

from car_collection.web.forms import CreateProfileForm, CreateCarForm, EditCarForm, DeleteCarForm, EditProfileForm, \
    DeleteProfileForm
from car_collection.web.models import Profile, Car


def get_profile():
    profile = Profile.objects.first()
    return profile


# Create your views here.
def index(request):
    profile = get_profile()

    context = {
        'profile': profile
    }
    return render(request, 'web/index.html', context)


def catalogue(request):
    profile = get_profile()

    if not profile:
        return redirect('home')

    cars = Car.objects.all()
    context = {
        'profile': profile,
        'cars': cars,
    }
    return render(request, 'web/catalogue.html', context)


def car_create(request):
    profile = get_profile()

    if not profile:
        return redirect('home')

    if request.method == 'GET':
        form = CreateCarForm()
    else:
        form = CreateCarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'web/car-create.html', context)


def car_details(request, pk):
    profile = get_profile()

    if not profile:
        return redirect('home')

    car = Car.objects.filter(pk=pk).get()
    context = {
        'profile': profile,
        'car': car,
    }
    return render(request, 'web/car-details.html', context)


def car_edit(request, pk):
    profile = get_profile()

    if not profile:
        return redirect('home')

    car = Car.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = EditCarForm(instance=car)
    else:
        form = EditCarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {
        'profile': profile,
        'form': form,
        'car': car
    }
    return render(request, 'web/car-edit.html', context)


def car_delete(request, pk):
    profile = get_profile()

    if not profile:
        return redirect('home')

    car = Car.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = DeleteCarForm(instance=car)
    else:
        form = DeleteCarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {
        'profile': profile,
        'form': form,
        'car': car
    }
    return render(request, 'web/car-delete.html', context)


def profile_create(request):
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
    return render(request, 'web/profile-create.html', context)


def profile_details(request):
    profile = get_profile()

    if not profile:
        return redirect('home')

    cars = Car.objects.all()
    total_price = sum(car.price for car in cars)

    context = {
        'profile': profile,
        'car': cars,
        'total_price': total_price
    }
    return render(request, 'web/profile-details.html', context)


def profile_edit(request):
    profile = get_profile()

    if not profile:
        return redirect('home')

    if request.method == 'GET':
        form = EditProfileForm(instance=profile)
    else:
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')
    context = {
        'profile': profile,
        'form': form,

    }
    return render(request, 'web/profile-edit.html', context)


def profile_delete(request):
    profile = get_profile()

    if not profile:
        return redirect('home')

    if request.method == 'GET':
        form = DeleteProfileForm(instance=profile)
    else:
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            Car.objects.all().delete()
            return redirect('home')
    context = {
        'profile': profile,
        'form': form,

    }
    return render(request, 'web/profile-delete.html', context)
