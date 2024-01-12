# api/serializers.py
from ninja import Schema
from ninja.orm import create_schema
from typing import List, Optional
from pydantic import BaseModel
from datetime import date

from rest_framework import serializers
from inab.models import Classroom, School, Nilam, User


class RoleSchema(Schema):
    role: str


class UserSchema(Schema):
    username: str
    name: str
    birthDate: date
    phoneNo: str
    email: str
    classID: int
    role: RoleSchema
    awardList: int


class UsernameSchema(Schema):
    username: str


class SchoolSchema(Schema):
    id: int
    name: str


class ClassroomSchema(Schema):
    name: str
    description: str
    schoolID: SchoolSchema


class LibrarySchema(Schema):
    schoolID: SchoolSchema
    librarianID: UserSchema


class BookSchema(Schema):
    title: str
    pages: int
    author: str
    genre: str
    publisher: str
    insertedAt: date
    updatedAt: Optional[str] = None
    deletedAt: Optional[str] = None
    libraryID_id: int


class TeacherSchema(Schema):
    username: str
    name: str
    birthDate: str
    phoneNo: str
    email: str
    awardList: int


class StudentSchema(Schema):
    username: str
    name: str
    birthDate: str
    phoneNo: str
    email: str
    awardList: int


class ClassroomDetailSchema(BaseModel):
    id: int
    name: str
    description: str
    teacher: Optional[dict]
    students: List[dict]


class NilamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nilam
        fields = "__all__"


class NilamCreateSchema(Schema):
    title: str
    pages: int
    author: str
    genre: str
    publisher: str
    studentID: str
    evaluationComment: str = None
    evaluationStatus: str = None


class NilamSchema(Schema):
    title: str
    pages: int
    author: str
    genre: str
    publisher: str
    # studentID_id_id: UsernameSchema
    evaluationComment: Optional[str] = None
    evaluationStatus: Optional[str] = None
