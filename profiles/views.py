from django.shortcuts import render

# Create your views here.

from .forms import ProfileCreateForm, RawProfileForm
from .models import Profile


def dynamic_lookup_view(request, profile_id):
    obj = Profile.objects.get(id=profile_id)
    context = {
        "object": obj
    }
    return render(request, "profile_detail.html", context)


def profile_create_view(request):
    form = RawProfileForm()
    if request.method == "POST":
        RawProfileForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            # data is good
            Profile.objects.create(**form.cleaned_data)
        else:
            print(form.errors)
    context = {
        'form': form
    }
    return render(request, "profile_create.html", context)


def profile_create_view(request):
    print("I am here")
    form = ProfileCreateForm(request.POST or None)
    if form.is_valid():
        print("valid form submission")
        form.save()
    else:
        print("not valid")
    context = {
        'form': form
    }
    return render(request, "profile_create.html", context)


def profile_detail_view(request):
    obj = Profile.objects.get(id=1)
    context = {
        'object': obj
    }
    return render(request, "profile_detail.html", context)
