from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


def login_programmatically(request):
    print("here friend")
    username = request.session.get('username')
    password = request.session.get('password')
    print(username, password)
    from django.contrib.auth import authenticate, login
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class Login(generic.CreateView):
    template_name = 'login_form.html'
