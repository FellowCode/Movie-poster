# Generated by Django 2.1.4 on 2018-12-08 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0004_session_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.Room'),
        ),
    ]