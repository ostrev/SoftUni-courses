from django.shortcuts import render, redirect

from .forms import CreateProfileForm, CreateAlbumForm, EditAlbumForm, DeleteAlbumForm, ProfileForm, DeleteProfileForm
from .models import Profile, Album


def get_profile():
    profile = Profile.objects.first()
    return profile


def get_album(pk):
    album = Album.objects.filter(pk=pk).get()
    return album


def index(request):
    profile = get_profile()

    if not profile:
        return redirect('profile add')

    albums = Album.objects.all()

    context = {
        'albums': albums,
        'profile': profile,
    }

    return render(request, 'web/home-with-profile.html', context)


def album_add(request):
    if request.method == 'GET':
        form = CreateAlbumForm()
    else:
        form = CreateAlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form,
    }
    return render(request, 'web/add-album.html', context)


def album_details(request, pk):
    album = get_album(pk)

    context = {
        'album': album,
    }
    return render(request, 'web/album-details.html', context)


def album_edit(request, pk):
    album = get_album(pk)
    if request.method == 'GET':
        form = EditAlbumForm(instance=album)
    else:
        form = EditAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'album': album,
        'form': form
    }

    return render(request, 'web/edit-album.html', context)


def album_delete(request, pk):
    album = get_album(pk)
    if request.method == 'GET':
        form = DeleteAlbumForm(instance=album)
    else:
        form = DeleteAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'album': album,
        'form': form,
    }

    return render(request, 'web/delete-album.html', context)


def profile_add(request):
    if get_profile() is not None:
        return redirect('home')

    if request.method == 'GET':
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'no_profile': True,
        'form': form
    }

    return render(request, 'web/home-no-profile.html', context)


def profile_details(request):
    profile = get_profile()
    albums_count = Album.objects.all().count()

    context = {
        'profile': profile,
        'albums_count': albums_count,
    }
    return render(request, 'web/profile-details.html', context)


def profile_delete(request):
    profile = get_profile()
    if request.method == 'GET':
        form = DeleteProfileForm(instance=profile)
    else:
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            Album.objects.all().delete()
            return redirect('home')

    context = {
        'form': form,
    }
    return render(request, 'web/profile-delete.html', context)
