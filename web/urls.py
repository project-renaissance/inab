"""
URL configuration for inab project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from . import views

urlpatterns = [
    path("", views.DashboardView.as_view(), name="dashboard"),
    path("student", views.StudentView.as_view(), name="student"),
    path("teacher", views.TeacherView.as_view(), name="teacher"),
    path("login", views.LoginView.as_view(), name="login"),
    path("profile", views.ProfileView.as_view(), name="profile"),
    path("register", views.RegisterView.as_view(), name="register"),
    path("book", views.BookView.as_view(), name="book"),
    path("book-request", views.BookRequestView.as_view(), name="book-request"),
    path("school", views.SchoolView.as_view(), name="school"),
]
