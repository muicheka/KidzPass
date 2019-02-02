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

from pages.views import home_view, contact_view, admin_view, user_view, about_view, hash_test
from profiles.views import (
    profile_detail_view,
    profile_create_view,
    dynamic_lookup_view,
    login_form_view,
)
from images.views import dynamic_lookup_view_images

urlpatterns = [
    path('', home_view, name='home'),
    path('contact/', contact_view, name='contact'),
    path('about/', about_view, name='about'),
    path('admin/', admin_view),
    path('user/', user_view),
    path('admin_panel/', admin.site.urls),
    path('profile/<int:profile_id>/', dynamic_lookup_view, name='profile'),
    path('create/', profile_create_view, name='create'),
    # path('login/', login_form_view, name='login'),
    path('hash/', hash_test, name='hash'),

    path('image/<str:image_id>/', dynamic_lookup_view_images, name='image'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
]
