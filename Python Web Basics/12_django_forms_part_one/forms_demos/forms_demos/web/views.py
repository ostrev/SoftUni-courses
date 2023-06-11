from django.shortcuts import render
from django import forms
from .forms import PersonForm
from forms_demos.web.models import Person


class PersonModelForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        # exclude = ['is_happy']
        widgets = {
            'name': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Your name',
                }
            )
        }

# Create your views here.
# class PersonForm(forms.Form):
#     your_name = forms.CharField(
#         label='Your name',
#         max_length=50,
#         required=False,
#         # widget=forms.Textarea(),
#         widget=forms.TextInput(
#             attrs={
#                 'placeholder': 'Your name',
#                 'class': 'form-control',
#             })
#     )
#
#     age = forms.IntegerField(
#         initial='22',
#         required=False,
#         help_text='Please fill Your age',
#     )
#
#     # email = forms.EmailField()
#     # password = forms.CharField()
#     # # password2 = forms.PasswordInput()
#     # password3 = forms.CharField(widget=forms.PasswordInput)
#     #
#     # url_input = forms.URLField()
#     # url_input_two = forms.CharField(widget=forms.URLField)
#     #
#     # date_input = forms.DateField()
#
#     HOBBY_CHOICES = [
#         (1, 'Football'),
#         (2, 'Basketball'),
#         (3, 'Tennis'),
#     ]
#
#     hobby = forms.ChoiceField(choices=HOBBY_CHOICES, widget=forms.RadioSelect )
#     # hobby2 = forms.CharField(widget=forms.Select(choices=HOBBY_CHOICES), )
#
#     is_happy = forms.BooleanField()
def index(request):
    name = None
    if request.method == 'POST':
        # print(request.POST)
        form = PersonForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']

            #     can create model from cleaned data!!!
            #     Person.objects.create(**form.cleaned_data)

            # other ways to create is are
            Person.objects.create(
                name=form.cleaned_data['your_name'],
                age=form.cleaned_data['age'],
                hobby=form.cleaned_data['hobby'],
                is_happy=form.cleaned_data['is_happy'],
            )

            # Person(
            #     name=form.cleaned_data['your_name'],
            #     age=form.cleaned_data['age'],
            # ).save()

        print(request.POST)
        print(form.cleaned_data)
    else:  # GET request
        form = PersonForm()

    context = {
        'form': form,
        'name': name,
    }
    return render(request, 'web/index.html', context)


def model_form_view(request):
    # make instance and fill the form
    # person = Person.objects.get(id=2)
    # context = {
    #     'model_form': PersonModelForm(instance=person),
    # }

    form = PersonModelForm()

    if request.method == "POST":
        form = PersonModelForm(request.POST)
        if form.is_valid():
            form.save()
            form = PersonModelForm()
    context = {
        'model_form': form,
    }

    return render(request, 'web/model_form.html', context)


def model_form_update(request, pk):
    person = Person.objects.get(pk=pk)
    form = PersonModelForm(instance=person)

    if request.method == "POST":
        form = PersonModelForm(request.POST, instance=person)
        if form.is_valid():
            form.save()


    context = {
        'model_form': form,
        'person': person
    }

    return render(request, 'web/model_form_update.html', context)
