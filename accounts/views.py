from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


def login_programmatically(request):
    username = request.session.get('username')
    password = request.session.get('password')
    from django.contrib.auth import authenticate, login
    if username and password:
        user = authenticate(username=username, password=password)
        print(authenticate(username=username, password=password))
        if user is not None:
            if user.is_active:
                print("logging in")
                login(request, user)
            else:
                print("Account deleted or disabled")
        else:
            print("didn't log in")
    return render(request, "home.html")


class Signup(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')

    template_name = 'registration/signup.html'


class Login(generic.CreateView):
    template_name = 'login_form.html'
