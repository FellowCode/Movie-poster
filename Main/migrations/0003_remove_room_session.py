# Generated by Django 2.1.4 on 2018-12-08 06:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0002_room'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='session',
        ),
    ]