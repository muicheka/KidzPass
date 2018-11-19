from django.shortcuts import render
from django.contrib import messages

# Create your views here.

from .forms import ProfileCreateForm, RawProfileForm
from .models import Profile


def dynamic_lookup_view(request, profile_id):
    obj = Profile.objects.get(id=profile_id)
    context = {
        "object": obj
    }
    return render(request, "profile_detail.html", context)




def login_form_view(request):
    form = ProfileCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
    else:
        print(form.errors)
    context = {
        'form': form
    }
    # (TO DO) not working
    return render(request, "login_form.html", context)


def profile_create_view(request):
    form = ProfileCreateForm(request.POST or None)
    if form.is_valid():
        messages.info(request, 'Successfully registered!')
        form.save()
    else:
        print("Not valid")
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


# def profile_create_view(request):
#     form = RawProfileForm()
#     if request.method == "POST":
#         RawProfileForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             # data is good
#             Profile.objects.create(**form.cleaned_data)
#         else:
#             print(form.errors)
#     context = {
#         'form': form
#     }
#     return render(request, "profile_create.html", context)