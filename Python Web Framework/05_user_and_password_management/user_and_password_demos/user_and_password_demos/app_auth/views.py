from django import forms

from django.contrib.auth import views as auth_views, login, get_user_model
from django.contrib.auth import mixins as auth_mixins
from django.contrib.auth import forms as auth_forms
from django.urls import reverse_lazy
from django.views import generic as views
from django.utils.translation import gettext_lazy as _

UserModel = get_user_model()


# this is how to customize the registration form
class RegisterUserForm(auth_forms.UserCreationForm):
    consent = forms.BooleanField()

    password2 = forms.CharField(
        label=_("Repeat password"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text=_("Repeat password, please"),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = _('It works ')


class RegisterUserView(views.CreateView):
    # model = ''
    template_name = 'app_auth/register.html'
    form_class = RegisterUserForm
    # static way to providing success url
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        user_data = form.cleaned_data
        print(user_data)

        # user = authenticate(username=user_data['username'], password=user_data['password1'])
        login(self.request, self.object)
        return result

    # Dynamic way to provide form, according to conditions
    # def get_form_class(self):
    #     if condition1:
    #         return conditionForm1
    #     else:
    #         return conditionForm2

    # dynamic way to providing success url
    # def get_success_url(self):
    #     pass


class LoginUserView(auth_views.LoginView):
    template_name = 'app_auth/login.html'
    # extra_context = {'title': 'login', 'link_title': 'Register'}
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()

        kwargs['initial'] = {
            'password': 'm1nk0v$!'
        }

        return kwargs

class LogoutUserView(auth_views.LogoutView):
    model = UserModel
    template_name = 'app_auth/logout.html'


class UserListView(auth_mixins.LoginRequiredMixin, views.ListView):
    model = UserModel
    template_name = 'app_auth/list_view.html'
    # login_url = reverse_lazy('login user')
    # write this code in settings.py for global redirect to for 'login'


class ViewWithPermission(auth_mixins.PermissionRequiredMixin, views.TemplateView):
    template_name = 'app_auth/list_view.html'
