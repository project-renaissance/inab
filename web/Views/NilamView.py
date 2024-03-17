from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from ..forms import BookRequestForm
from django.http import JsonResponse
from inab.models import Library, Borrow


class BookRequestView(View):
    template_name = "pages/Nilam/book-request.html"

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
    template_name = "pages/Nilam/add_book_request.html"

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
