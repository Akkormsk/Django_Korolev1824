# Generated by Django 4.0.4 on 2022-07-18 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='courses',
            options={'verbose_name': 'Курс', 'verbose_name_plural': 'Курсы'},
        ),
        migrations.AlterModelOptions(
            name='lessons',
            options={'verbose_name': 'Урок', 'verbose_name_plural': 'Уроки'},
        ),
        migrations.AlterModelOptions(
            name='teachers',
            options={'verbose_name': 'Учитель', 'verbose_name_plural': 'Учителя'},
        ),
    ]
