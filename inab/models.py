from django.db import models

class School(models.Model):
	name = models.CharField(max_length=255)

class Classroom(models.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255)
	schoolID = models.ForeignKey(School, on_delete=models.CASCADE)

class Role(models.Model):
	RoleType = [
		('student', 'student'),
		('teacher', 'teacher'),
		('guruNilam', 'guruNilam'),
	]
	role = models.CharField(primary_key=True, choices=RoleType)

class User(models.Model):
	username = models.CharField(max_length=255, primary_key=True)
	name = models.CharField(max_length=255)
	birthDate = models.DateField(null=True)
	phoneNo = models.CharField(max_length=255, null=True)
	email = models.EmailField()
	classID = models.ForeignKey(Classroom, on_delete=models.CASCADE)
	role = models.ManyToManyField(Role)
	awardList = models.IntegerField()

class Library(models.Model):
	schoolID = models.ForeignKey(School, on_delete=models.CASCADE)
	librarianID = models.ForeignKey(User, on_delete=models.CASCADE)

class Book(models.Model):
	GENRE = [
		('action', 'action'),
		('fantasy', 'fantasy'),
	]
	title = models.CharField(max_length=255)
	pages = models.IntegerField()
	author = models.CharField(max_length=255)
	genre = models.CharField(max_length=255, choices=GENRE)
	publisher = models.CharField(max_length=255)
	insertedAt = models.DateField()
	updatedAt = models.DateField(null=True)
	deletedAt = models.DateField(null=True)
	libraryID = models.ForeignKey(Library, on_delete=models.CASCADE)

class Nilam(models.Model):
	title = models.CharField(max_length=255)
	pages = models.IntegerField()
	author = models.CharField(max_length=255)
	genre = models.CharField(max_length=255)
	publisher = models.CharField(max_length=255)
	studentID = models.ForeignKey(User, on_delete=models.CASCADE)
	evaluationComment = models.CharField(max_length=255, null=True)
	evaluationStatus = models.CharField(max_length=255, null=True)

class Borrow(models.Model):
	bookID = models.ForeignKey(Book, on_delete=models.CASCADE)
	borrowStatus = models.BooleanField(default=True)
	date = models.DateField()
	borrowReport = models.CharField(max_length=255)
	studentID = models.ForeignKey(User, on_delete=models.CASCADE)

class GameProfile(models.Model):
	studentID = models.ForeignKey(User, on_delete=models.CASCADE)
	rank = models.CharField(max_length=255)
	record = models.CharField(max_length=255)
	characterList = models.CharField(max_length=255)
	itemList = models.CharField(max_length=255)

