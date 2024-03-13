from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class School(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Classroom(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Role(models.Model):
    RoleType = [
        ("student", "student"),
        ("teacher", "teacher"),
        ("guruNilam", "guruNilam"),
    ]
    role = models.CharField(choices=RoleType, max_length=50)


class User(AbstractUser):
    name = models.CharField(max_length=255)
    birthDate = models.DateField(null=True)
    phoneNo = models.CharField(max_length=255, blank=True)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, null=True)
    role = models.ManyToManyField(Role)
    awardList = models.IntegerField(null=True)

    # Add related_name to avoid clashes
    groups = models.ManyToManyField(Group, related_name="inab_user_groups")
    user_permissions = models.ManyToManyField(
        Permission, related_name="inab_user_permissions"
    )


class Library(models.Model):
    name = models.CharField(max_length=255)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    librarians = models.ManyToManyField(User)


class Book(models.Model):
    GENRE = [
        ("action", "action"),
        ("fantasy", "fantasy"),
    ]
    title = models.CharField(max_length=255)
    pages = models.IntegerField(null=True)
    author = models.CharField(max_length=255, blank=True)
    genre = models.CharField(max_length=255, choices=GENRE, blank=True)
    publisher = models.CharField(max_length=255, blank=True)
    insertedAt = models.DateField(auto_now_add=True)
    updatedAt = models.DateField(null=True)
    deletedAt = models.DateField(null=True)
    library = models.ManyToManyField(Library)

    def __str__(self):
        return self.title


class Nilam(models.Model):
    title = models.CharField(max_length=255)
    pages = models.IntegerField(null=True)
    author = models.CharField(max_length=255, blank=True)
    genre = models.CharField(max_length=255, blank=True)
    publisher = models.CharField(max_length=255, blank=True)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    evaluationComment = models.CharField(max_length=255, blank=True)
    evaluationStatus = models.CharField(max_length=255, blank=True)


class Borrow(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowStatus = models.BooleanField(default=True)
    date = models.DateField()
    borrowReport = models.CharField(max_length=255, blank=True)
    student = models.ForeignKey(User, on_delete=models.CASCADE)


class GameProfile(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    rank = models.CharField(max_length=255, blank=True)
    record = models.CharField(max_length=255, blank=True)
    characterList = models.CharField(max_length=255, blank=True)
    itemList = models.CharField(max_length=255, blank=True)
