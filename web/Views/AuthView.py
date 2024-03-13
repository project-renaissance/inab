from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views import View
from django.core.serializers import serialize
from inab.models import Book, Borrow, School, User, Library
from ..forms import BookForm, SchoolForm, StudentRegistrationForm


class LoginView(View):
    template_name = "pages/Auth/login.html"

    def get(self, request, *args, **kwargs):
        context = {
            "active_page": "login",  # Set the active page for the dashboard view
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        return redirect("/")
        # email_or_name = request.POST.get('email_or_name')
        # password = request.POST.get('password')

    # Try to authenticate the user
    # user = authenticate(request, email=email_or_name, password=password)

    # if user is not None:
    #     login(request, user)
    #     messages.success(request, 'Login successful. Welcome back!')
    # Redirect to a success page or dashboard
    # return redirect('/')
    # else:
    # Handle invalid login
    # messages.error(request, 'Invalid login credentials. Please try again.')
    # print("Form errors:", request.POST.get('email_or_name'), request.POST.get('password'))
    # return render(request, self.template_name, {'active_page': 'login'})


class LogoutView(View):
    template_name = "pages/Auth/logout.html"

    def get(self, request, *args, **kwargs):
        context = {
            "active_page": "login",  # Set the active page for the dashboard view
        }
        return render(request, self.template_name, context)


class RegisterView(View):
    template_name = "pages/Auth/register.html"

    def get(self, request, *args, **kwargs):
        form = StudentRegistrationForm()
        context = {
            "active_page": "register",
            "form": form,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Add login logic if needed
            return redirect("login")  # Redirect to the login page
        else:
            # Handle form validation errors
            context = {
                "active_page": "register",
                "form": form,
            }
            return render(request, self.template_name, context)
