from django import forms

from music_app.web.models import Profile, Album


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class CreateProfileForm(ProfileForm):
    class Meta:
        model = Profile
        fields = '__all__'


class DeleteProfileForm(ProfileForm):
    class Meta:
        model = Profile
        fields = []

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        widgets = {
            'album_name': forms.TextInput(attrs={'placeholder': 'Album Name', }),
            'artist': forms.TextInput(attrs={'placeholder': 'Artist', }),
            'description': forms.Textarea(attrs={'placeholder': 'Description', }),
            'image_url': forms.URLInput(attrs={'placeholder': 'Image URL', }),
            'price': forms.NumberInput(attrs={'placeholder': 'Price', }), }


class CreateAlbumForm(AlbumForm):
    class Meta:
        model = Album
        fields = '__all__'


class EditAlbumForm(AlbumForm):
    class Meta:
        model = Album
        fields = '__all__'


class DeleteAlbumForm(AlbumForm):
    class Meta:
        model = Album
        fields = '__all__'

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, fild in self.fields.items():
            fild.widget.attrs['disabled'] = 'disabled'
            fild.required = False
