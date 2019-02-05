from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


def login_programmatically(request):
    username = request.session.get('username')
    password = request.session.get('password')
    from django.contrib.auth import authenticate, login
    if username and password:
        user = authenticate(username=username, password=password)
        print(authenticate(username=username, password=password))
        if user is not None:
            print("logging in")
            login(request, user)
        else:
    return render(request, "home.html")


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class Login(generic.CreateView):
    template_name = 'login_form.html'
