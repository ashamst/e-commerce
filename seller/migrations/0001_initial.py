# Generated by Django 3.1.5 on 2021-03-17 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product_tb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('name', models.CharField(max_length=20)),
                ('details', models.CharField(max_length=20)),
                ('stock', models.CharField(max_length=20)),
                ('price', models.CharField(max_length=20)),
            ],
        ),
    ]