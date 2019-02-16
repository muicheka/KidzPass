from django.shortcuts import redirect, render
from django.http import HttpResponse
import base64
import datetime


def get_current_time():
    currentDT = datetime.datetime.now()
    return currentDT


def home_view(request, *args, **kwargs):
    print(get_current_time())
    print("LOGGED IN AS: ")
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


def graphical_login_view(request, *args, **kwargs):
    # return HttpResponse("<h1>About page</h1>")  # string of HTML code
    return render(request, "graphical_login.html", {})


def reguser(request, *args, **kwargs):
    return render(request, "reg_select_user.html", {})


def hash_test(request):
    image_id = request.POST.get('password_image_id')
    import base64
    with open("static/images/PasswordImages/" + image_id, "rb") as imageFile:
        str = base64.b64encode(imageFile.read())
    request.session['password'] = str
    username = request.session.get('username')
    print(get_current_time())
    print("LOGIN:")
    print("Username:")
    print(request.session.get('username'))
    print("Password:")
    print(request.session.get('password'))
    print("Password Image number:")
    print(image_id)
    return render(request, "registration/login.html", {
        'username': username,
        'password': str})


def reg_hash(request):
    image_id = request.POST.get('password_image_id')
    path = "static/images/PasswordImages/" + image_id
    with open(path, "rb") as imageFile:
        str = base64.b64encode(imageFile.read())
    request.session['password'] = str
    username = request.session.get('username')
    print(get_current_time())
    print("REGISTER:")
    print("Username:")
    print(request.session.get('username'))
    print("Password:")
    print(request.session.get('password'))
    print("Password Image number:")
    print(image_id)

    return render(request, "registration/signup.html", {
        'username': username,
        'password': str})


def username_select_view(request):
    return render(request, "username_selection.html")


usernames = {
    1: "elephant",
    2: "rhino",
    3: "rabbit",
    4: "bear",
    5: "koala",
    6: "panda",
    7: "chicken",
    8: "penguin",
    9: "frog",
    10: "snake",
    11: "whale",
    12: "dolphin",
    13: "shark",
    14: "octopus",
    15: "butterfly",
    16: "ladybird",
    17: "spider",
    18: "bee",
    19: "monkey",
    20: "dog",
    21: "fox",
    22: "cat",
    23: "lion",
    24: "tiger",
    25: "horse",
    26: "zebra",
    27: "cow",
    28: "pig",
    29: "giraffe",
    30: "fish",
    31: "turtle",
    32: "crocodile",
    33: "owl",
    34: "bird",
    35: "gorilla",
}


def selected_user_image_reg_view(request):
    user_image_id = request.POST.get('user_image_id')
    user_image_id = user_image_id.replace(".JPG", "")
    user_image_id = int(user_image_id)

    current_username = usernames[user_image_id]
    request.session['username'] = current_username
    return render(request, "select_graphical_password.html", {
        'username': current_username,
    })


def selected_user_image_view(request):
    user_image_id = request.POST.get('user_image_id')
    user_image_id = user_image_id.replace(".JPG", "")
    user_image_id = int(user_image_id)

    current_username = usernames[user_image_id]
    request.session['username'] = current_username
    return render(request, "graphical_login.html", {
        'username': current_username,
    })


def get_user_image(request):
    target_user = request.session.get('username')
    image_location = 0
    for x in usernames:
        if usernames[x] == target_user:
            image_location = x
        else:
            print("image not found")
    if image_location != 0:
        string = "/static/images/UserImages/" + str(image_location) + ".JPG"
        return string


from django.shortcuts import render_to_response
import json
from django.core import serializers


def testcall(request):
    from django.contrib.auth.models import User

    print(get_current_time())
    print("STARTED REGISTRATION")
    users = User.objects.all()
    list_users = [entry for entry in users]
    data = serializers.serialize('json', list_users)
    return HttpResponse(data)


from django.contrib import messages