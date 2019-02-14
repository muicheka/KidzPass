"""Django_GraphicalPasswords URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from accounts.views import login_programmatically, Login, Signup
from pages.views import (
    home_view,
    contact_view,
    admin_view, user_view,
    graphical_login_view,
    hash_test,
    reg_hash,
    username_select_view,
    selected_user_image_view,
    get_user_image,
    testcall,
    reguser,
    selected_user_image_reg_view,
    game_view

)
from profiles.views import (
    profile_detail_view,
    profile_create_view,
    dynamic_lookup_view,
    login_form_view,
)

urlpatterns = [
    path('', home_view, name='home'),
    path('contact/', contact_view, name='contact'),
    path('graphical_login/', graphical_login_view, name='graphical_login'),
    path('admin/', admin_view),
    path('user/', user_view),
    path('admin_panel/', admin.site.urls),
    path('profile/<int:profile_id>/', dynamic_lookup_view, name='profile'),
    path('create/', profile_create_view, name='create'),
    # path('login/', login_form_view, name='login'),
    path('hash/', hash_test, name='hash'),
    path('reg_hash/', reg_hash, name='reg_hash'),
    path('get_user_image', get_user_image, name='get_user_image'),

    path('reguser/testcall/', testcall, name="testcall"),
    path('reguser/', reguser, name='reguser'),
    path('loginprog/', login_programmatically, name='login_prog'),
    path('username/', username_select_view, name='username_select'),
    path('selected_user/', selected_user_image_view, name='selected_user_image'),
    path('selected_user_reg/', selected_user_image_reg_view, name='selected_user_image_reg'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/login/', Login, name='Login'),
    path('accounts/signup/', Signup, name='Signup'),

    path('game/', game_view, name='game'),

]

urlpatterns += staticfiles_urlpatterns()
