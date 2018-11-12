from django import forms

from .models import Profile


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'f_name',
            's_name',
            'dob'
        ]


class RawProfileForm(forms.Form):
    f_name = forms.CharField()
    s_name = forms.CharField()
    dob = forms.DateField()
