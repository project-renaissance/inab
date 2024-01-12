from ninja import Router
from django.shortcuts import get_object_or_404
from inab.models import School, Classroom, Book, User, Role, Nilam
from ninja.errors import HttpError

from typing import List
from .serializers import (
    ClassroomSchema,
    BookSchema,
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


# 1: Module Classroom
# Get All Student Lists
@router.get("/student", response=List[StudentSchema])
def list_students(request, role: str = "student"):
    students = User.objects.filter(role__role=role)

    # Convert birthDate to string for each student
    for student in students:
        student.birthDate = str(student.birthDate)

    return students


# Get Student Details
@router.get("/student/{username}", response=StudentSchema)
def get_student(request, username: str):
    student = get_object_or_404(User, username=username, role__role="student")

    # Convert birthDate to string
    student.birthDate = str(student.birthDate)

    return student


# Get Schools List
@router.get("/school", response=List[SchoolSchema])
def school_list(request):
    schools = School.objects.all()
    return schools


# Get Classrooms List
@router.get("/classroom-list", response=List[ClassroomSchema])
def classroom_list(request):
    classrooms = Classroom.objects.all()
    return classrooms


# Get List of student on Classroom, & Classroom's Teacher
@router.get("classroom", response=List[ClassroomDetailSchema])
def list_classrooms(request):
    classrooms = Classroom.objects.all()
    classroom_details = []

    for classroom in classrooms:
        teacher = User.objects.filter(classID=classroom, role__role="teacher").first()
        students = User.objects.filter(classID=classroom, role__role="student")

        classroom_data = {
            "id": classroom.id,
            "name": classroom.name,
            "description": classroom.description,
            "teacher": None,
            "students": [],
        }

        if teacher:
            classroom_data["teacher"] = {
                "username": teacher.username,
                "name": teacher.name,
                "birthDate": str(teacher.birthDate),
                "phoneNo": teacher.phoneNo,
                "email": teacher.email,
                "awardList": teacher.awardList,
            }

        classroom_serializer = ClassroomDetailSchema(**classroom_data)
        classroom_details.append(classroom_serializer.dict())

    return classroom_details


@router.get("classroom/{id}", response=ClassroomDetailSchema)
def get_classroom(request, id: int):
    classroom = Classroom.objects.filter(id=id).first()

    if not classroom:
        raise HttpError(404, "Not Found")

    teacher = User.objects.filter(classID=classroom, role__role="teacher").first()
    students = User.objects.filter(classID=classroom, role__role="student")

    classroom_data = {
        "id": classroom.id,
        "name": classroom.name,
        "description": classroom.description,
        "teacher": None,
        "students": [],
    }

    if teacher:
        classroom_data["teacher"] = {
            "username": teacher.username,
            "name": teacher.name,
            "birthDate": str(teacher.birthDate),
            "phoneNo": teacher.phoneNo,
            "email": teacher.email,
            "awardList": teacher.awardList,
        }

    classroom_serializer = ClassroomDetailSchema(**classroom_data)
    return classroom_serializer.model_dump()


# 2: Library
# Get Books List
@router.get("/book", response=List[BookSchema])
def list_books(request):
    books = Book.objects.all()
    return books


# 3: Nilam
# Get Nilams List


@router.get("/nilam", response=List[NilamSchema])
def list_nilam(request):
    nilams = Nilam.objects.all()
    return nilams


# Insert Nilam
# @router.post("/nilam", response=List[NilamSerializer])
# # @permission_classes([IsAuthenticated])
# def create_nilam(request, data: NilamCreateSchema):
#     # Check if the user is a teacher
#     if not request.user.role.filter(role="teacher").exists():
#         return Response(
#             {"error": "Only teachers can create Nilam records."},
#             status=status.HTTP_403_FORBIDDEN,
#         )

#     serializer = NilamSerializer(data=data.dict())
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
