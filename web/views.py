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


# class StudentView(View):
#     template_name = "pages/student.html"

#     def get(self, request, *args, **kwargs):
#         users = User.objects.all()

#         user_list = list(users)

#         context = {
#             "name": "Student",
#             "active_page": "student",
#             "user_list": user_list,
#         }

#         return render(request, self.template_name, context)


# class StudentView(View):
#     template_name = "pages/student.html"

#     def get(self, request, *args, **kwargs):
#         school_id = request.GET.get("school_id")
#         classroom_id = request.GET.get("classroom_id")

#         schools = School.objects.all()
#         classrooms = Classroom.objects.all()
#         students = User.objects.all()

#         if school_id:
#             # If school_id is present, filter classrooms and students based on the selected school
#             selected_school = School.objects.get(id=school_id)
#             classrooms = Classroom.objects.filter(school=selected_school)
#             students = User.objects.filter(classroom__in=classrooms)

#         return render(
#             request,
#             self.template_name,
#             {
#                 "students": students,
#                 "classrooms": classrooms,
#                 "schools": schools,
#                 "school_id": school_id,
#             },
#         )


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


class AddBookRequestView(View):
    template_name = "pages/add_book_request.html"

    def get(self, request, *args, **kwargs):
        form = BookRequestForm()
        libraries = Library.objects.all()
        return render(
            request, self.template_name, {"form": form, "libraries": libraries}
        )

    def post(self, request, *args, **kwargs):
        form = BookRequestForm(request.POST)
        print(form.__dict__)
        # print(form)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True})  # Return success as a JSON response
        else:
            errors = form.errors
            print(errors)

            return JsonResponse({"success": False, "errors": errors}, status=400)


def approveBorrowRequest(request, borrow_id):
    borrow_instance = get_object_or_404(Borrow, id=borrow_id)

    # Perform the approval logic, set borrowStatus to True
    borrow_instance.borrowStatus = True
    borrow_instance.save()

    return JsonResponse({"message": "Borrow request approved successfully"})


def disapprove_borrow_request(request, borrow_id):
    borrow_instance = get_object_or_404(Borrow, id=borrow_id)

    # Perform the disapproval logic, set borrowStatus to False
    borrow_instance.borrowStatus = False
    borrow_instance.save()

    return JsonResponse({"message": "Borrow request disapproved successfully"})


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
