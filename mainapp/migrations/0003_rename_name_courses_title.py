# Generated by Django 4.0.4 on 2022-07-21 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_alter_courses_options_alter_lessons_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courses',
            old_name='name',
            new_name='title',
        ),
    ]
