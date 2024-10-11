# Generated by Django 5.1.1 on 2024-10-05 07:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cooking', '0007_subject_subjectmarks'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reportcard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_rank', models.IntegerField()),
                ('result_date', models.DateField(auto_now_add=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_rank', to='Cooking.student')),
            ],
            options={
                'unique_together': {('student_rank', 'result_date')},
            },
        ),
    ]