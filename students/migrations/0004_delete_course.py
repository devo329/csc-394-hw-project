# Generated by Django 4.1.5 on 2023-01-28 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_alter_student_first_name_alter_student_last_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Course',
        ),
    ]
