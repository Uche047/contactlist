"""contactlist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from contact.views import index_view, addContact_view, profile_view, editContact_view, delete_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index_view, name='index'),
    path('add/', addContact_view, name='add-contact'),
    path('profile/<int:id>/', profile_view, name='profile'),
    path('edit/<int:id>/', editContact_view, name='edit'),
    path('delete/<int:id>/', delete_view, name='delete'),
]
