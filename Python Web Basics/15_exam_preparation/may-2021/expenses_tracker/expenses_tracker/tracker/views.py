from django.shortcuts import render, redirect

from expenses_tracker.core.profil_help_func import get_profile, get_profile_and_budget
from expenses_tracker.tracker.forms import EditExpenseForm, CreateExpenseForm, DeleteExpenseForm, \
    CreateProfileForm, EditProfileForm, DeleteProfileForm
from expenses_tracker.tracker.models import Profile, Expense


# Create your views here.
def home_page(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')

    profile = get_profile_and_budget()

    expenses = Expense.objects.all()
    context = {
        'expenses': expenses,
        'budget': profile.budget,
        'budget_left': profile.budget_left,
    }
    return render(request, 'tracker/home-with-profile.html', context)


def create_expense(request):
    if request.method == 'GET':
        form = CreateExpenseForm()
    else:
        form = CreateExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form
    }

    return render(request, 'tracker/expense-create.html', context)


def edit_expense(request, pk):
    expense = Expense.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = EditExpenseForm(instance=expense)
    else:
        form = EditExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form': form,
        'expense': expense,
    }

    return render(request, 'tracker/expense-edit.html', context)


def delete_expense(request, pk):
    expense = Expense.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = DeleteExpenseForm(instance=expense)
    else:
        expense.delete()
        return redirect('home')
    context = {
        'form': form,
        'expense': expense,
    }

    return render(request, 'tracker/expense-delete.html', context)


def profile(request):
    profile = get_profile_and_budget()

    context = {
        'profile': profile,
    }

    return render(request, 'tracker/profile.html', context)


def profile_create(request):
    if request.method == 'GET':
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form
    }

    return render(request, 'tracker/home-no-profile.html', context)


def profile_edit(request):
    profile = get_profile()
    if request.method == 'GET':
        form = EditProfileForm(instance=profile)
    else:
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')

    content = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'tracker/profile-edit.html', content)


def profile_delete(request):
    profile = get_profile()
    if request.method == 'GET':
        form = DeleteProfileForm()
    else:
        profile.delete()
        Expense.objects.all().delete()
        return redirect('home')

    return render(request, 'tracker/profile-delete.html')

