# Generated by Django 2.1.4 on 2018-12-08 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0009_auto_20181208_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='room',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Main.Room'),
        ),
    ]