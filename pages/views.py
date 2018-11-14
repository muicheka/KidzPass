from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home_view(request, *args, **kwargs):
    print(request.user)
    my_context = {
        "title": "Welcome to the home page",
        "user_list": [1, 2, 3, 4, 5, 6, 7],
    }
    return render(request, "home.html", my_context)


def contact_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Contact page</h1>")  # string of HTML code
    return render(request, "contact.html", {})


def user_view(request, *args, **kwargs):
    # return HttpResponse("<h1>User Page</h1>")  # string of HTML code
    return render(request, "user.html", {})


def admin_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Admin page</h1>")  # string of HTML code
    return render(request, "admin.html", {})


def about_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Contact page</h1>")  # string of HTML code
    return render(request, "about.html", {})