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


class DisabledFormMixin:
    disabled_fields = ()
    fields = {}

    def _disable_fields(self):
        if self.disabled_fields == '__all__':
            fields = self.fields.keys()
        else:
            fields = self.disabled_fields
        for field_name in fields:
            if field_name in self.fields:
                field = self.fields[field_name]
                # field.widget.attrs['disabled'] = 'disabled'
                field.widget.attrs['readonly'] = 'readonly'


class PetDeleteForm(DisabledFormMixin, PetBaseForm):
    disabled_fields = ('name', 'date_of_birth', 'personal_photo',)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()

    def save(self, commit=True):
        super().save()
        if commit:
            self.instance.delete()
        else:
            pass
        return self.instance

    # def __disable_fields(self):
    #     for name, field in self.fields.items():
    #         field.widget.attrs['disabled'] = 'disabled'
    #         field.widget.attrs['readonly'] = 'readonly'
