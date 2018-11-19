from django import forms
import datetime

from .models import Profile


class ProfileCreateForm(forms.ModelForm):
    f_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={"placeholder": "First Name"}))
    s_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={"placeholder": "Second Name"}))
    dob = forms.DateField(widget=forms.SelectDateWidget(years=range(1940, 2013)), label='Date of Birth')
    # format='%d-%m-%Y'
    password = forms.DecimalField
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={"placeholder": "Username"}))

    class Meta:
        model = Profile
        fields = [
            'username',
            'f_name',
            's_name',
            'dob',
            'password',
            'admin',

        ]

    # hoping to generate usernames from random series of numbers (TO DO)
    def generate_username(self):
        random_number = Profile.objects.make_random_password(length=10, allowed_chars='1234567890')
        self.username = random_number

    # currently not working (TO DO)
    def clean_dob(self):
        dob = self.cleaned_data.get("dob")
        print(dob)
        print(datetime.date.today())
        if dob == datetime.date.today():
            raise forms.ValidationError("This is not a valid date of birth")
        else:
            return dob


class RawProfileForm(forms.Form):
    f_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={"placeholder": "First Name"}))
    s_name = forms.CharField(label='Last Name')
    dob = forms.DateField(label='Date of Birth', initial=datetime.date.today())

