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
from .Views import BookView as bookViews
from .Views import SchoolView as schoolViews
from .Views import AuthView as authViews
from .Views import TeacherView as teacherViews
from .Views import NilamView as nilamViews

# from .views import approveBorrowRequest, disapprove_borrow_request


book_urls = [
    path("book", bookViews.BookView.as_view(), name="book"),
    path(
        "update_book/<int:book_id>/", bookViews.UpdateBook.as_view(), name="update_book"
    ),
    path(
        "delete_book/<int:book_id>/", bookViews.DeleteBook.as_view(), name="delete_book"
    ),
    path("add_book", bookViews.AddBookView.as_view(), name="add_book"),
    path("search_books/", bookViews.search_books, name="search_books"),
    path(
        "get_book/<int:book_id>/",
        bookViews.GetBookDetails.as_view(),
        name="get_book_details",
    ),
]

school_urls = [
    path("school", schoolViews.SchoolView.as_view(), name="school"),
    path("add_school", schoolViews.AddSchoolView.as_view(), name="add_school"),
    path(
        "update_school/<str:school_name>/",
        schoolViews.UpdateSchool.as_view(),
        name="update_book",
    ),
]

nilam_urls = [
    path("book-request", nilamViews.BookRequestView.as_view(), name="book-request"),
    path(
        "add_book_request",
        nilamViews.AddBookRequestView.as_view(),
        name="add_book_request",
    ),
    path(
        "approve_borrow/<int:borrow_id>/",
        nilamViews.approveBorrowRequest,
        name="approve_borrow_request",
    ),
    path(
        "disapprove_borrow/<int:borrow_id>/",
        nilamViews.disapprove_borrow_request,
        name="disapprove_borrow_request",
    ),
]

teacher_urls = [
    path("teacher", teacherViews.TeacherView.as_view(), name="teacher"),
    path("add_teacher", teacherViews.AddTeacherView.as_view(), name="add_teacher"),
]

student_urls = []

auth_urls = [
    path("login", authViews.LoginView.as_view(), name="login"),
    path("register", authViews.RegisterView.as_view(), name="register"),
    path("logout", authViews.LogoutView.as_view(), name="logout"),
]

urlpatterns = [
    path("", views.DashboardView.as_view(), name="dashboard"),
    path("student", views.StudentView.as_view(), name="student"),
    # Use the unpacking operator to include the Book URLs
    *auth_urls,
    *book_urls,
    *school_urls,
    *nilam_urls,
    *teacher_urls,
    path("student", views.StudentView.as_view(), name="student"),
    # path("teacher", views.TeacherView.as_view(), name="teacher"),
    path("profile", views.ProfileView.as_view(), name="profile"),
    path("get_libraries/", views.GetLibrariesView.as_view(), name="get_libraries"),
]
