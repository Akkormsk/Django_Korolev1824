# Generated by Django 4.0.4 on 2022-06-18 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_remove_courses_body_as_markdown_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='courses',
            options={'ordering': ('-created_at',)},
        ),
        migrations.AlterModelOptions(
            name='lessons',
            options={'ordering': ('-created_at',)},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'новость', 'verbose_name_plural': 'новости'},
        ),
        migrations.AlterModelOptions(
            name='teachers',
            options={'ordering': ('-created_at',)},
        ),
    ]
