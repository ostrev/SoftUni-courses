from django import forms
from .models import Pet

class PetBaseForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = '__all__'
        exclude = ('slug',)
        labels = {
            'name': 'Pet Name:',
            'date_of_birth': 'Data of Birth:',
            'personal_photo': 'Link to Image:',
        }

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Pet name'
                }
            ),
            'personal_photo': forms.URLInput(
                attrs={
                    'placeholder': 'Link to image'
                }
            ),
            'date_of_birth': forms.DateInput(
                attrs={
                    'placeholder': 'mm/dd/yyyy',
                    "type": "date"
                }
            )
        }
class PetCreateForm(PetBaseForm):
    pass


class PetEditForm(PetBaseForm):
    pass


class PetDeleteForm(PetBaseForm):
    pass
