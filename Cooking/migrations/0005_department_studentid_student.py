# Generated by Django 5.1.1 on 2024-10-03 05:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cooking', '0004_recipeform_recipe_counter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='studentID',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
                ('student_email', models.EmailField(max_length=254, unique=True)),
                ('student_age', models.IntegerField(default=18)),
                ('student_address', models.TextField()),
                ('Department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='depart', to='Cooking.department')),
                ('student_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='studentid', to='Cooking.studentid')),
            ],
            options={
                'verbose_name': 'student',
                'ordering': ['student_name'],
            },
        ),
    ]
