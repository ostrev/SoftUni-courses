from django import forms

from petstagram.photos.models import Photo


class PhotoBaseForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'
        exclude = ('date_of_publication',)


class PhotoCreateForm(PhotoBaseForm):
    pass


class PhotoEditForm(PhotoBaseForm):
    class Meta:
        model = Photo
        fields = '__all__'
        exclude = ('date_of_publication', 'photo')


class PhotoDeleteForm(PhotoBaseForm):
    pass
