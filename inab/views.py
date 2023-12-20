from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View

class DashboardView(View):
    template_name = 'pages/dashboard.html'

    def get(self, request, *args, **kwargs):
        context = {
            'active_page': 'dashboard',  # Set the active page for the dashboard view
        }
        return render(request, self.template_name, context)

class StudentView(View):
    template_name = 'pages/student.html'

    def get(self, request, *args, **kwargs):
        context = {
            'active_page': 'student',  # Set the active page for the dashboard view
        }
        return render(request, self.template_name, context)

class TeacherView(View):
    template_name = 'pages/teacher.html'

    def get(self, request, *args, **kwargs):
        context = {
            'active_page': 'teacher',  # Set the active page for the dashboard view
        }
        return render(request, self.template_name, context)
        
class LoginView(View):
    template_name = 'pages/login.html'

    def get(self, request, *args, **kwargs):
        context = {
            'active_page': 'login',  # Set the active page for the dashboard view
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        return redirect('/')
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
    template_name = 'pages/profile.html'

    def get(self, request, *args, **kwargs):
        context = {
            'active_page': 'profile',  # Set the active page for the dashboard view
        }
        return render(request, self.template_name, context)

class RegisterView(View):
    template_name = 'pages/register.html'

    def get(self, request, *args, **kwargs):
        form = StudentRegistrationForm()
        context = {
            'active_page': 'register',
            'form': form,
        }
        return render(request, self.template_name, context)
        
    def post(self, request, *args, **kwargs):
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Add login logic if needed
            return redirect('login')  # Redirect to the login page
        else:
            # Handle form validation errors
            context = {
                'active_page': 'register',
                'form': form,
            }
            return render(request, self.template_name, context)