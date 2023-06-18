from django.shortcuts import render, redirect

from expenses_tracker.tracker.forms import CreateProfileForm, CreateExpenseForm, EditExpenseForm, \
    DeleteExpenseForm, EditProfileForm, DeleteProfileForm
from expenses_tracker.tracker.models import Profile, Expense


def get_profile():
    profile = Profile.objects.first()

    if profile:
        expenses = Expense.objects.all()
        profile.budget_left = profile.budget - sum(e.price for e in expenses)
        profile.bought_items = expenses.count()
    return profile


def home(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')
        # return render(request, 'tracker/home-no-profile.html')

    expenses = Expense.objects.all()

    context = {
        'profile': profile,
        'expenses': expenses,
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
        'expense': expense
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
        'expense': expense
    }

    return render(request, 'tracker/expense-delete.html', context)


def profile(request):
    profile = get_profile()

    context = {
        'profile': profile
    }
    return render(request, 'tracker/profile.html', context)


def create_profile(request):
    if request.method == 'GET':
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form,
        'no_profile': True,
    }
    return render(request, 'tracker/home-no-profile.html', context)


def edit_profile(request):
    profile = get_profile()
    if request.method == "GET":
        form = EditProfileForm(instance=profile)
    else:
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')

    context = {
        'form': form,

    }
    return render(request, 'tracker/profile-edit.html', context)


def delete_profile(request):
    profile = get_profile()
    if request.method == "GET":
        form = DeleteProfileForm(instance=profile)
    else:
        form = DeleteProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            Expense.objects.all().delete()
            return redirect('home')

    context = {
        'form': form,
    }
    return render(request, 'tracker/profile-delete.html', context)


# this is easier way
# profile = get_profile()
    # if request.method == 'POST':
    #     profile.delete()
    #     Expense.objects.all().delete()
    #     return redirect('home')
    #
    # return render(request, 'tracker/profile-delete.html')
