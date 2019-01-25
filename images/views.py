from django.shortcuts import render
from .models import Image


def dynamic_lookup_view_images(request, image_id):
    obj = Image.objects.get(id=image_id)
    context = {
        "object": obj
    }
    return render(request, "image_page.html", context)