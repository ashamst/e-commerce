# Generated by Django 3.1.5 on 2021-03-12 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register_tb',
            old_name='adress',
            new_name='address',
        ),
    ]