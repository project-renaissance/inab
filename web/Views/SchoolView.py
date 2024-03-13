from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views import View
from django.core.serializers import serialize
from inab.models import Book, Borrow, School, User, Library
from ..forms import BookForm, SchoolForm


class SchoolView(View):
    template_name = "pages/School/school.html"

    def get(self, request, *args, **kwargs):
        schools = School.objects.all()

        school_list = list(schools)

        context = {
            "name": "List of School ",
            "active_page": "school",
            "school_list": school_list,
        }

        return render(request, self.template_name, context)


class AddSchoolView(View):
    template_name = "pages/School/add_school.html"

    def get(self, request, *args, **kwargs):
        form = SchoolForm()
        libraries = Library.objects.all()
        return render(
            request, self.template_name, {"form": form, "libraries": libraries}
        )

    def post(self, request, *args, **kwargs):
        form = SchoolForm(request.POST)
        print(form.__dict__)
        # print(form)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True})  # Return success as a JSON response
        else:
            errors = form.errors
            print(errors)

            return JsonResponse({"success": False, "errors": errors}, status=400)


class UpdateSchool(View):
    template_name = "pages/School/school.html"

    def post(self, request, book_id):

        book = get_object_or_404(Book, id=book_id)
        form = BookForm(request.POST, instance=book)

        if form.is_valid():
            form.save()
            response_data = {
                "status": "Success",
                "message": "Book updated successfully",
            }
        else:
            response_data = {"status": "Fail", "errors": form.errors}

        return JsonResponse(response_data)
