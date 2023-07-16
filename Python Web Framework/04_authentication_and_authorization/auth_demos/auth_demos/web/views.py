import random

from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views import generic as views

UserModel = get_user_model()


class AuthView(views.TemplateView, LoginRequiredMixin):
    template_name = 'index-two.html'
    model = UserModel
    login_url = reverse_lazy('login')


    def get_context_data(self, **kwargs):
        pass


# this is not good way, login_url=reverse_lazy('login')
# better is to write LOGIN_URL = reverse_lazy('login') in settings.py
@login_required(login_url=reverse_lazy('login'))
def index(request):
    suffix = random.randint(1, 100)

    # # Password is not hash!!
    # UserModel.objects.create(
    #     username=f'ostrev_{suffix}',
    #     password='test1234'
    # )

    # Password is  hash by create_user method -> make_password!!
    # UserModel.objects.create_user(
    #     username=f'ostrev_{suffix}',
    #     password='test1234'
    # )

    ostrev_84 = UserModel.objects.get(username='ostrev_84')
    context = {
        'user': request.user,
        'permission': request.user.has_perm('auth.view_user'),
        'ostrev_84': ostrev_84.has_perm('auth.view_user')
    }
    return render(request, 'index.html', context)


def login_user(request):
    # Authenticate
    user = authenticate(
        username=f'ostrev_84',
        password='test1234'
    )
    print(f'Authenticate user: {user}')

    # Authorization
    login(request, user)
    return redirect('index')


def logout_user(request):
    logout(request)
    return redirect('index')
