from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from inab.models import Book, Borrow, School, User


class DashboardView(View):
    template_name = "pages/dashboard.html"

    def get(self, request, *args, **kwargs):
        users = User.objects.all()

        user_list = list(users)

        context = {
            "name": "Dashboard",
            "active_page": "dashboard",
            "user_list": user_list,
        }

        return render(request, self.template_name, context)


class BookView(View):
    template_name = "pages/book.html"

    def get(self, request, *args, **kwargs):
        books = Book.objects.all()

        book_list = list(books)

        context = {
            "name": "List of Books",
            "active_page": "book",
            "book_list": book_list,
        }

        return render(request, self.template_name, context)


class BookRequestView(View):
    template_name = "pages/book-request.html"

    def get(self, request, *args, **kwargs):
        borrow = Borrow.objects.all()

        borrow_list = list(borrow)

        context = {
            "name": "Borrow Records ",
            "active_page": "book-request",
            "borrow_list": borrow_list,
        }

        return render(request, self.template_name, context)


class SchoolView(View):
    template_name = "pages/school.html"

    def get(self, request, *args, **kwargs):
        schools = School.objects.all()

        school_list = list(schools)

        context = {
            "name": "List of School ",
            "active_page": "school",
            "school_list": school_list,
        }

        return render(request, self.template_name, context)


class StudentView(View):
    template_name = "pages/student.html"

    def get(self, request, *args, **kwargs):
        context = {
            "active_page": "student",  # Set the active page for the dashboard view
        }
        return render(request, self.template_name, context)


class TeacherView(View):
    template_name = "pages/teacher.html"

    def get(self, request, *args, **kwargs):
        context = {
            "active_page": "teacher",  # Set the active page for the dashboard view
        }
        return render(request, self.template_name, context)


class LoginView(View):
    template_name = "pages/login.html"

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


class ProfileView(View):
    template_name = "pages/profile.html"

    def get(self, request, *args, **kwargs):
        context = {
            "active_page": "profile",  # Set the active page for the dashboard view
        }
        return render(request, self.template_name, context)


class RegisterView(View):
    template_name = "pages/register.html"

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
