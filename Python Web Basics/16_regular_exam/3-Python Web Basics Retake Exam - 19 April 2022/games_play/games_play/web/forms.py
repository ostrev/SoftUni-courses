from django import forms

from games_play.web.models import Profile, Game


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['email', 'age', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }


class CreateProfileForm(ProfileForm):
    pass


class EditProfileForm(ProfileForm):
    class Meta:
        password = forms.CharField(widget=forms.PasswordInput)
        model = Profile
        fields = ['email', 'age', 'password', 'first_name', 'last_name', 'profile_image']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'profile_image': 'Profile Picture',
        }
        widgets = {
            'password': forms.PasswordInput(render_value=True),
        }


class DeleteProfileForm(ProfileForm):
    class Meta:
        model = Profile
        fields = []

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = "__all__"


class CreateGameForm(GameForm):
    pass


class EditGameForm(GameForm):
    pass


class DeleteGameForm(GameForm):
    class Meta:
        model = Game
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance
