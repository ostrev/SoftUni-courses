import uuid

from django import forms
from django.core.exceptions import ValidationError

from .models_validators import validate_max_todos_per_person
from .validators import validate_text, ValueInRangeValidator
from .models import Todo, Person


class TodoForm(forms.Form):
    text = forms.CharField(
        max_length=30,
        validators=(
            validate_text,
        ),
        error_messages={
            'required': 'Todo text must be set!'
        }
    )
    is_done = forms.BooleanField(required=False)

    priority = forms.IntegerField(
        validators=(
            ValueInRangeValidator(1, 10),
            # validate_priority,
            # MinValueValidator(1),
            # MaxValueValidator(10),
        )
    )

    # def clean_text(self):
    #     pass
    #
    # def clean_priority(self):
    #     # raise ValidationError('raise a error if the value is between 1 and 10')
    #     pass
    #
    # def clean_is_done(self):
    #     pass


class TodoCreateForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = '__all__'

    def clean(self):
        return super().clean()

    def clean_text(self):
        return self.cleaned_data['text'].lower()
    """
    Used for:
    1. Transform data into desired format/form
    2. Validation
    """
    # # validate if assignee has more than MAX_COUNT
    # def clean_assignee(self):
    #     # print(self.cleaned_data['assignee'])
    #     assignee = self.cleaned_data['assignee']
    #     validate_max_todos_per_person(assignee)
    #     return assignee

    # validate if person has more than MAX_COUNT_TODOS
    # if the person is not free, assignee to another person
    def clean_assignee(self):
        assignee = self.cleaned_data['assignee']
        try:
            validate_max_todos_per_person(assignee)
        except ValidationError:
            assignee = Person.objects.get(name='Unassigned')

        return assignee


class PersonCreateForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

    def clean_profile_image(self):
        profile_image = self.cleaned_data['profile_image']
        profile_image = str(uuid.uuid4())
        return profile_image

    # # if we want to use person name for img name.
    # def clean(self):
    #     super().clean() # after this all values are in cleaned_data
    #     profile_image = self.cleaned_data['profile_image']
    #     profile_image.name = self.cleaned_data['name']
    #     return profile_image
