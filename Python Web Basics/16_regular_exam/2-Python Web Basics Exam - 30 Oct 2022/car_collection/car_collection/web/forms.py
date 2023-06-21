from django import forms

from car_collection.web.models import Profile, Car


class ProfileForm(forms.ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Profile
        fields = ['username', 'email', 'age', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }


class CreateProfileForm(ProfileForm):
    pass


class EditProfileForm(ProfileForm):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'age', 'password', 'first_name', 'last_name', 'profile_picture']
        widgets = {
            'password': forms.PasswordInput(),
        }
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'profile_picture': 'Profile Picture',
        }


class DeleteProfileForm(ProfileForm):
    class Meta:
        model = Profile
        fields = []

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"


class CreateCarForm(CarForm):
    pass


class EditCarForm(CarForm):
    pass


class DeleteCarForm(CarForm):
    class Meta:
        model = Car
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
