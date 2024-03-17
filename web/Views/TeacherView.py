from django.shortcuts import render, redirect, get_object_or_404
from django.views import View


class TeacherView(View):
    template_name = "pages/Teacher/teacher.html"

    def get(self, request, *args, **kwargs):
        context = {
            "active_page": "teacher",  # Set the active page for the dashboard view
        }
        return render(request, self.template_name, context)


class AddTeacherView(View):
    template_name = "pages/Teacher/add_teacher.html"

    def get(self, request, *args, **kwargs):
        context = {
            "active_page": "add_teacher",  # Set the active page for the dashboard view
        }
        return render(request, self.template_name, context)
