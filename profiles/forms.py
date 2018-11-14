from django import forms
import datetime

from .models import Profile


class ProfileCreateForm(forms.ModelForm):
    f_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={"placeholder": "First Name"}))
    s_name = forms.CharField(label='Last Name')
    dob = forms.DateField(widget=forms.SelectDateWidget(years=range(1940, 2013)), label='Date of Birth')
    # format='%d-%m-%Y'
    password = forms.DecimalField

    class Meta:
        model = Profile
        fields = [
            'f_name',
            's_name',
            'dob',
            'password',
            'admin',
            'summary'
        ]

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
