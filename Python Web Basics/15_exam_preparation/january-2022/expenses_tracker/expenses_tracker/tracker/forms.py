import os

from django import forms

from expenses_tracker.tracker.models import Profile, Expense


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('budget', 'first_name', 'last_name', 'profile_image')
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'profile_image': 'Profile Image'
        }



class CreateProfileForm(ProfileForm):
    pass


class EditProfileForm(ProfileForm):
    pass


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        image_path = self.instance.profile_image.path

        self.instance.delete()
        os.remove(image_path)
        return self.instance

    class Meta:
        model = Profile
        fields = ()


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['title', 'description', 'expense_image', 'price']
        labels = {
            'expense_image': 'Link to Image',
        }

class CreateExpenseForm(ExpenseForm):
    pass


class EditExpenseForm(ExpenseForm):
    pass


class DeleteExpenseForm(ExpenseForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
            field.widget.attrs['disabled'] = 'disabled'
