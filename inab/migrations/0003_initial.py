# Generated by Django 4.2.8 on 2023-12-21 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inab', '0002_remove_student_school_remove_teacher_classroom_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('pages', models.IntegerField()),
                ('author', models.CharField(max_length=255)),
                ('genre', models.CharField(choices=[('action', 'action'), ('fantasy', 'fantasy')], max_length=255)),
                ('publisher', models.CharField(max_length=255)),
                ('insertedAt', models.DateField()),
                ('updatedAt', models.DateField(null=True)),
                ('deletedAt', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('role', models.CharField(choices=[('student', 'student'), ('teacher', 'teacher'), ('guruNilam', 'guruNilam')], primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('birthDate', models.DateField(null=True)),
                ('phoneNo', models.CharField(max_length=255, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('awardList', models.IntegerField()),
                ('classID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inab.classroom')),
                ('role', models.ManyToManyField(to='inab.role')),
            ],
        ),
        migrations.CreateModel(
            name='Nilam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('pages', models.IntegerField()),
                ('author', models.CharField(max_length=255)),
                ('genre', models.CharField(max_length=255)),
                ('publisher', models.CharField(max_length=255)),
                ('evaluationComment', models.CharField(max_length=255, null=True)),
                ('evaluationStatus', models.CharField(max_length=255, null=True)),
                ('studentID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inab.user')),
            ],
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('librarianID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inab.user')),
                ('schoolID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inab.school')),
            ],
        ),
        migrations.CreateModel(
            name='GameProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.CharField(max_length=255)),
                ('record', models.CharField(max_length=255)),
                ('characterList', models.CharField(max_length=255)),
                ('itemList', models.CharField(max_length=255)),
                ('studentID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inab.user')),
            ],
        ),
        migrations.AddField(
            model_name='classroom',
            name='schoolID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inab.school'),
        ),
        migrations.CreateModel(
            name='Borrow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrowStatus', models.BooleanField(default=True)),
                ('date', models.DateField()),
                ('borrowReport', models.CharField(max_length=255)),
                ('bookID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inab.book')),
                ('studentID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inab.user')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='libraryID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inab.library'),
        ),
    ]
