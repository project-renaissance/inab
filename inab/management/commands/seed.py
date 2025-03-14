from django.core.management.base import BaseCommand
from faker import Faker
from random import choice, sample
from django.utils import timezone
from inab.models import (
    School,
    Classroom,
    Role,
    User,
    Library,
    Book,
    Nilam,
    Borrow,
    GameProfile,
)

fake = Faker()


class Command(BaseCommand):
    help = "Seed the database with dummy data"

    def handle(self, *args, **options):
        self.create_schools()
        self.create_classrooms()
        # self.create_roles()
        self.create_users()
        self.create_libraries()
        self.create_books()
        self.create_nilams()
        self.create_borrows()
        self.create_game_profiles()

    def create_schools(self):
        School.objects.bulk_create([School(name=fake.company()) for _ in range(5)])

    def create_classrooms(self):
        schools = School.objects.all()
        classrooms = [
            Classroom(
                name=fake.word(), description=fake.sentence(), schoolID=choice(schools)
            )
            for _ in range(20)
        ]
        Classroom.objects.bulk_create(classrooms)

    # def create_roles():
    #     roles = [role[0] for role in Role.RoleType]
    #     Role.objects.bulk_create([Role(role=r) for r in roles])

    def create_users(self):
        classrooms = Classroom.objects.all()
        roles = Role.objects.all()

        users = []
        for _ in range(50):
            user = User(
                username=fake.user_name(),
                name=fake.name(),
                birthDate=fake.date_of_birth(),
                phoneNo=fake.phone_number(),
                email=fake.email(),
                classID=choice(classrooms),
                awardList=fake.random_int(0, 100),
            )
            user.save()
            user.role.set(sample(list(roles), fake.random_int(1, 3)))

    def create_libraries(self):
        schools = School.objects.all()
        librarians = User.objects.filter(role__role="teacher")

        libraries = [
            Library(schoolID=choice(schools), librarianID=choice(librarians))
            for _ in range(5)
        ]
        Library.objects.bulk_create(libraries)

    def create_books(self):
        libraries = Library.objects.all()
        genres = ["action", "fantasy"]

        books = [
            Book(
                title=fake.word(),
                pages=fake.random_int(100, 500),
                author=fake.name(),
                genre=choice(genres),
                publisher=fake.company(),
                insertedAt=timezone.now(),
                libraryID=choice(libraries),
            )
            for _ in range(50)
        ]
        Book.objects.bulk_create(books)

    def create_nilams(self):
        users = User.objects.filter(role__role="student")

        nilams = [
            Nilam(
                title=fake.word(),
                pages=fake.random_int(50, 200),
                author=fake.name(),
                genre=choice(["action", "fantasy"]),
                publisher=fake.company(),
                studentID=choice(users),
                evaluationComment=fake.sentence(),
                evaluationStatus=choice(["pending", "approved", "rejected"]),
            )
            for _ in range(20)
        ]
        Nilam.objects.bulk_create(nilams)

    def create_borrows(self):
        books = Book.objects.all()
        students = User.objects.filter(role__role="student")

        borrows = [
            Borrow(
                bookID=choice(books),
                borrowStatus=choice([True, False]),
                date=timezone.now(),
                borrowReport=fake.sentence(),
                studentID=choice(students),
            )
            for _ in range(30)
        ]
        Borrow.objects.bulk_create(borrows)

    def create_game_profiles(self):
        students = User.objects.filter(role__role="student")

        game_profiles = [
            GameProfile(
                studentID=choice(students),
                rank=fake.word(),
                record=fake.sentence(),
                characterList=fake.words(5),
                itemList=fake.words(3),
            )
            for _ in range(20)
        ]
        GameProfile.objects.bulk_create(game_profiles)
