from django.shortcuts import render

# Create your views here.

from .forms import ProfileCreateForm
from .models import Profile


def profile_create_view(request):
    form = ProfileCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProfileCreateForm()
    context = {
        'form': form
    }
    return render(request, "profile_create.html", context)


def profile_detail_view(request):
    obj = Profile.objects.get(id=1)
    context={
        'object': obj
    }
    return render(request, "profile_detail.html", context)
