from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views import View
from django.core.serializers import serialize
from inab.models import Book, Borrow, School, User, Library
from ..forms import BookForm, SchoolForm


class GetBookDetails(View):

    def get(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        data = {
            "title": book.title,
            "author": book.author,
            "pages": book.pages,
            "genre": book.genre,
        }
        return JsonResponse(data)


class UpdateBook(View):
    template_name = "pages/Book/book.html"

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


class DeleteBook(View):

    def post(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        book.delete()
        return JsonResponse({"success": True})


class AddBookView(View):
    template_name = "pages/Book/add_book.html"

    def get(self, request, *args, **kwargs):
        form = BookForm()
        libraries = Library.objects.all()
        return render(
            request, self.template_name, {"form": form, "libraries": libraries}
        )

    def post(self, request, *args, **kwargs):
        form = BookForm(request.POST)
        print(form.__dict__)
        # print(form)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True})  # Return success as a JSON response
        else:
            errors = form.errors
            print(errors)

            return JsonResponse({"success": False, "errors": errors}, status=400)


def search_books(request):
    if request.method == "POST":
        search_term = request.POST.get("search", "")
        books = Book.objects.filter(title__icontains=search_term)
        book_data = [
            {
                "title": book.title,
                "author": book.author,
                "genre": book.genre,
                "pages": book.pages,
            }
            for book in books
        ]
        return JsonResponse(book_data, safe=False)
    return JsonResponse([], safe=False)


class BookView(View):
    template_name = "pages/Book/book.html"

    def get(self, request, *args, **kwargs):
        books = Book.objects.all()

        book_list = list(books)

        context = {
            "name": "List of Books",
            "active_page": "book",
            "book_list": book_list,
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        # Handle book creation here
        form = BookForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("book")  # Redirect to the book list page

        # If form is not valid, re-render the page with errors
        context = {
            "name": "List of Books",
            "active_page": "book",
            "book_list": Book.objects.all(),
            "form": form,
        }

        return render(request, self.template_name, context)

    def put(self, request, *args, **kwargs):
        # Handle book update here
        book_id = kwargs.get("book_id")
        book = get_object_or_404(Book, id=book_id)
        form = BookForm(request.PUT or None, instance=book)

        if form.is_valid():
            form.save()
            return redirect("book")  # Redirect to the book list page

        # If form is not valid, re-render the page with errors
        context = {
            "name": "List of Books",
            "active_page": "book",
            "book_list": Book.objects.all(),
            "form": form,
        }

        return render(request, self.template_name, context)

    def delete(self, request, *args, **kwargs):
        # Handle book deletion here
        book_id = kwargs.get("book_id")
        book = get_object_or_404(Book, id=book_id)
        book.delete()
        return redirect("book")  # Redirect to the book list page


class SaveBookView(View):
    template_name = "pages/Book/book.html"

    def post(self, request, *args, **kwargs):
        form = BookForm(request.POST)
        if form.is_valid():
            # Save the form data to the database or perform any necessary action
            form.save()
            return redirect("book_list")  # Redirect to the book list page
        else:
            # Handle form validation errors if needed
            return render(request, self.template_name, {"form": form})
