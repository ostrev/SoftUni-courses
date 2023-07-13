from django.shortcuts import render
from django.templatetags.static import static
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, login, get_user_model

from petstagram.accounts.forms import RegisterUserForm, LoginUserForm, ProfileEditForm
from petstagram.accounts.models import PetstagramUser

UserModel = get_user_model()
class RegisterUserView(views.CreateView):
    model = PetstagramUser
    form_class = RegisterUserForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)

        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['next'] = self.request.GET.get('next', self.success_url)

        return context

    def get_success_url(self):
        return self.request.POST.get('next', self.success_url)


class LoginUserView(auth_views.LoginView):
    form_class = LoginUserForm
    template_name = 'accounts/login-page.html'


class LogoutUserView(auth_views.LogoutView):
    next_page = reverse_lazy('login user')


class ProfileDetailView(views.DetailView):
    template_name = 'accounts/profile-details-page.html'
    model = UserModel

    def get_context_data(self, **kwargs):
        profile_image = static('images/person.png')

        if self.object.profile_picture is not None:
            profile_image = self.object.profile_picture

        context = super().get_context_data(**kwargs)
        context['profile_image'] = profile_image
        context['pets'] = self.request.user.pet_set.all()

        return context


class ProfileEditView(views.UpdateView):
    model = PetstagramUser
    form_class = ProfileEditForm
    template_name = 'accounts/profile-edit-page.html'

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={'pk': self.object.pk})


class ProfileDeleteView(views.DeleteView):
    template_name = 'accounts/profile-delete-page.html'