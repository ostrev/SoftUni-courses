from django.shortcuts import render, redirect

from games_play.web.forms import CreateProfileForm, CreateGameForm, EditGameForm, DeleteGameForm, EditProfileForm, \
    DeleteProfileForm
from games_play.web.models import Profile, Game


def get_profile():
    profile = Profile.objects.first()
    return profile


def index(request):
    profile = get_profile()

    # if not profile:
    #     return redirect('home')

    context = {
        'profile': profile,
    }
    return render(request, 'web/home-page.html', context)


def dashboard(request):
    profile = get_profile()
    games = Game.objects.all()
    if not profile:
        return redirect('home')

    context = {
        'profile': profile,
        'games': games,
    }
    return render(request, 'web/dashboard.html', context)


def game_create(request):
    profile = get_profile()

    if not profile:
        return redirect('home')
    if request.method == 'GET':
        form = CreateGameForm()
    else:
        form = CreateGameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'web/create-game.html', context)


def game_details(request, pk):
    profile = get_profile()
    game = Game.objects.filter(pk=pk).get()
    if not profile:
        return redirect('home')

    context = {
        'profile': profile,
        'game': game

    }
    return render(request, 'web/details-game.html', context)


def game_edit(request, pk):
    profile = get_profile()
    
    if not profile:
        return redirect('home')
    game = Game.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = EditGameForm(instance=game)
    else:
        form = EditGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {
        'profile': profile,
        'form': form,
        'game': game,
    }
    return render(request, 'web/edit-game.html', context)


def game_delete(request, pk):
    profile = get_profile()

    if not profile:
        return redirect('home')

    game = Game.objects.filter(pk=pk).get()
    if not profile:
        return redirect('home')
    if request.method == 'GET':
        form = DeleteGameForm(instance=game)
    else:
        form = DeleteGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {
        'profile': profile,
        'form': form,
        'game': game
    }
    return render(request, 'web/delete-game.html', context)


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
            return redirect('home')

    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'web/create-profile.html', context)


def profile_details(request):
    profile = get_profile()
    if not profile:
        return redirect('home')

    games = Game.objects.all()
    total_games = Game.objects.all().count()
    average_rating = sum(r.rating for r in Game.objects.all())
    if average_rating == 0:
        average_rating = '0.0'

    context = {
        'profile': profile,
        'total_games': total_games,
        'average_rating': average_rating,
        'games': games
    }
    return render(request, 'web/details-profile.html', context)


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
    return render(request, 'web/edit-profile.html', context)


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
            Game.objects.all().delete()
            return redirect('home')
    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'web/delete-profile.html', context)
