from django import forms

from fruitipedia.web.models import Profile, Fruit


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email', 'password']


class CreateProfileForm(ProfileForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email', 'password']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name', }),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name', }),
            'email': forms.EmailInput(attrs={'placeholder': 'Email', }),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password', }),
        }

        labels = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'password': '',
        }


class EditProfileForm(ProfileForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'image', 'age']


class DeleteProfileForm(ProfileForm):
    class Meta:
        model = Profile
        fields = []

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance


class FruitForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = "__all__"


class CreateFruitForm(FruitForm):
    class Meta:
        model = Fruit
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Fruit Name', }),
            'image': forms.URLInput(attrs={'placeholder': 'Fruit Image URL', }),
            'description': forms.Textarea(attrs={'placeholder': 'Fruit Description', }),
            'nutrition': forms.Textarea(attrs={'placeholder': 'Nutrition Info', }),
        }
        labels = {
            'name': '',
            'image': '',
            'description': '',
            'nutrition': '',
        }


class EditFruitForm(FruitForm):
    pass


class DeleteFruitForm(FruitForm):
    class Meta:
        model = Fruit
        fields = ['name', 'image', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance
