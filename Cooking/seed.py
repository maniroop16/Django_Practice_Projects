from faker import Faker
import random
from Cooking.models import *
from django.db.models import Sum

# this is used to create fake data
fake = Faker()

# Seeding function will create details of the Student class
def seeding(n)->None:
    for i in range(n):
        all_departments = Department.objects.all()
        dep_index = random.randint(0, len(all_departments)-1)

        student_id = f"0{random.randint(100,999)}"

        department = all_departments[dep_index]
        student_name = fake.name()
        student_email = fake.email()
        student_age = random.randint(18,25)
        student_address = fake.address()

        #creating objects for Student and StudentID

        student_id_obj = studentID.objects.create(student_id = student_id)

        student_objs = Student.objects.create(
            Department = department,
            student_id = student_id_obj,
            student_name = student_name,
            student_email = student_email,
            student_age = student_age,
            student_address = student_address
            )

# This below Generate_marks function will generate random marks to particular subjects     
def Generate_marks(n):
    try:
        student_obj = Student.objects.all()
        for student in student_obj:
            subject_obj = Subject.objects.all()
            for subject in subject_obj:
                SubjectMarks.objects.create(
                    subject = subject, 
                    student = student, 
                    subjectmarks = random.randint(10,100)
                    )
    except Exception as e:
        print(e)

# The below generate_studentranks function is used to generate ranks 
# for students based on total marks
def generate_studentranks():
    ranks = Student.objects.annotate(marks = Sum('studentmarks__subjectmarks')).order_by("-marks")
    i = 1
    for rank in ranks:
        Reportcard.objects.create(
            student = rank,
            student_rank = i
            )
        i+=1
            
