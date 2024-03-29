# Generated by Django 5.0.2 on 2024-02-21 21:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Standard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('std_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('rollno', models.CharField(max_length=50)),
                ('course', models.CharField(max_length=20)),
                ('standard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_management.standard')),
            ],
        ),
    ]
