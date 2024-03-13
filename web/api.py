import api
from ninja import Router
from django.shortcuts import get_object_or_404
from inab.models import School, Classroom, Book, User, Role, Nilam
from ninja.errors import HttpError

from typing import List
from .serializers import (
    ClassroomSchema,
    BookSchema,
    BookSchemaResponse,
    ClassroomDetailSchema,
    SchoolSchema,
    NilamSerializer,
    NilamCreateSchema,
    StudentSchema,
    NilamSchema,
    RoleSchema,
)
from rest_framework import status
from pprint import pprint
from rest_framework.response import Response

router = Router()


# Book
@api.post("/book/create")
def create_book(request, payload: BookSchema):
    book = Book.objects.create(**payload.dict())
    return {"id": book.id}


@api.get("/book/{book_id}", response=BookSchemaResponse)
def get_book(request, book_id: int):
    book = get_object_or_404(Book, id=book_id)
    return book


@api.get("/book", response=List[BookSchemaResponse])
def list_books(request):
    qs = Book.objects.all()
    return qs


@api.patch("/book/{book_id}")
def update_book(request, book_id: int, payload: BookSchema):
    book = get_object_or_404(Book, id=book_id)
    for attr, value in payload.dict().items():
        # book.first_name = payload.first_name
        # book.last_name = payload.last_name
        # book.department_id = payload.department_id
        # book.birthdate = payload.birthdate

        setattr(book, attr, value)
    book.save()
    return {"success": True}


# Partial Update
# Partial updates

# To allow the user to make partial updates, use payload.dict(exclude_unset=True).items().
# This ensures that only the specified fields get updated.


@api.delete("/book/{book_id}")
def delete_book(request, book_id: int):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return {"success": True}
