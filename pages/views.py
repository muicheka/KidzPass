from django.shortcuts import redirect, render
from django.http import HttpResponse
import base64


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


def graphical_login_view(request, *args, **kwargs):
    # return HttpResponse("<h1>About page</h1>")  # string of HTML code
    return render(request, "graphical_login.html", {})


def reguser(request, *args, **kwargs):
    return render(request, "reg_select_user.html", {})


def hash_test(request):
    image_id = request.POST.get('image_id')
    import base64
    with open("static/images/"+image_id, "rb") as imageFile:
        str = base64.b64encode(imageFile.read())
    request.session['password'] = str
    username = request.session.get('username')
    print(request.session.get('username'))
    print(request.session.get('password'))
    return render(request, "registration/login.html", {
        'username': username,
        'password': str})


def reg_hash(request):
    image_id = request.POST.get('image_id')
    print(image_id)
    path = "static/images/UserImages/" + image_id
    with open(path, "rb") as imageFile:
        str = base64.b64encode(imageFile.read())
    request.session['password'] = str
    username = request.session.get('username')
    print(request.session.get('username'))
    print(request.session.get('password'))

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
    print("running")
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

    users = User.objects.all()
    list_users = [entry for entry in users]
    print(list_users)
    data = serializers.serialize('json', list_users)
    return HttpResponse(data)


from django.contrib import messages


def game_view(request):
    if request.user.is_authenticated:
        return render(request, "game.html")
    else:
        messages.info(request, "You are not authenticated yet")
        return render(request, "home.html")
