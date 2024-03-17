from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views import View
from django.core.serializers import serialize
from inab.models import Book, Borrow, School, User, Library, Classroom, Borrow
from .forms import BookForm, SchoolForm, StudentRegistrationForm, BookRequestForm


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


class StudentView(View):
    template_name = "pages/student.html"

    def get(self, request, *args, **kwargs):
        school_id = request.GET.get("school_id")
        print(school_id)
        classroom_id = request.GET.get("classroom_id")
        print(classroom_id)

        if school_id and classroom_id:
            print("if school and classroom id")
            selected_classroom = Classroom.objects.get(id=classroom_id)
            students = User.objects.filter(classroom=selected_classroom)
            return render(
                request,
                self.template_name,
                {
                    "students": students,
                    "school_id": school_id,
                    "classroom_id": classroom_id,
                    "selected_classroom": selected_classroom,
                },
            )
        elif school_id:
            print("if school")
            # If school_id is present, filter classrooms and students based on the selected school
            selected_school = School.objects.get(id=school_id)
            classrooms = Classroom.objects.filter(school=selected_school)
            return render(
                request,
                self.template_name,
                {
                    "classrooms": classrooms,
                    "selected_school": selected_school,
                    "school_id": school_id,
                },
            )
        else:
            # If no parameters are present, display only the list of schools
            schools = School.objects.all()
            return render(request, self.template_name, {"schools": schools})


class GetLibrariesView(View):
    def get(self, request, *args, **kwargs):
        libraries = Library.objects.values(
            "id", "name"
        )  # Fetch only the id and name fields
        return JsonResponse(list(libraries), safe=False)


class TeacherView(View):
    template_name = "pages/teacher.html"

    def get(self, request, *args, **kwargs):
        context = {
            "active_page": "teacher",  # Set the active page for the dashboard view
        }
        return render(request, self.template_name, context)


class ProfileView(View):
    template_name = "pages/profile.html"

    def get(self, request, *args, **kwargs):
        context = {
            "active_page": "profile",  # Set the active page for the dashboard view
        }
        return render(request, self.template_name, context)
