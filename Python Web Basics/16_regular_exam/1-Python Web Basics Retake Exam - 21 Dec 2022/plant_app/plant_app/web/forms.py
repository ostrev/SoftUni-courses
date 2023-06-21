from django import forms

from plant_app.web.models import Profile, Plant


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'first_name', 'last_name']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
        }


class CreateProfileForm(ProfileForm):
    pass


class EditProfileForm(ProfileForm):
    class Meta:
        model = Profile
        fields = ['username', 'first_name', 'last_name', 'profile_picture']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'profile_picture': 'Profile Picture'
        }


class DeleteProfileForm(ProfileForm):
    class Meta:
        model = Profile
        fields = []

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance


class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'
        labels = {
            'plant_type': 'Type',
            'name': 'Name',
            'image': 'Image URL',
        }


class CreatePlantForm(PlantForm):
    pass


class EditPlantForm(PlantForm):
    pass


class DeletePlantForm(PlantForm):
    class Meta:
        model = Plant
        fields = '__all__'
        labels = {
            'plant_type': 'Type',
            'name': 'Name',
            'image': 'Image URL',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False
    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance
