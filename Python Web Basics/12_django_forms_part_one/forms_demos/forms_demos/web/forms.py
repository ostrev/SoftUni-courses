from django import forms

class PersonForm(forms.Form):
    your_name = forms.CharField(
        label='Your name',
        max_length=50,
        required=False,
        # widget=forms.Textarea(),
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Your name',
                'class': 'form-control',
            })
    )

    age = forms.IntegerField(
        initial='22',
        required=False,
        help_text='Please fill Your age',
    )

    # email = forms.EmailField()
    # password = forms.CharField()
    # # password2 = forms.PasswordInput()
    # password3 = forms.CharField(widget=forms.PasswordInput)
    #
    # url_input = forms.URLField()
    # url_input_two = forms.CharField(widget=forms.URLField)
    #
    # date_input = forms.DateField()

    HOBBY_CHOICES = [
        (1, 'Football'),
        (2, 'Basketball'),
        (3, 'Tennis'),
    ]

    hobby = forms.ChoiceField(choices=HOBBY_CHOICES, widget=forms.RadioSelect )
    # hobby2 = forms.CharField(widget=forms.Select(choices=HOBBY_CHOICES), )

    is_happy = forms.BooleanField()