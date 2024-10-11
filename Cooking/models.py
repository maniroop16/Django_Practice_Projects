from django.db import models
from django.contrib.auth.models import User

# These are used for setting CustomUser model
#from django.contrib.auth import get_user_model
#User = get_user_model()


# Create your models here.

# This model is for creating Recipes
class Recipeform(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    Recipe_Name = models.CharField(max_length=100)
    Recipe_Description = models.TextField()
    Recipe_Image = models.ImageField(upload_to="cookingpage_images")
    Recipe_counter = models.IntegerField(default=1)


# These models are for creating Students and their details
class Department(models.Model):
    department = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.department
    
    class Meta:
        ordering = ['department']

class studentID(models.Model):
    student_id = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.student_id   

# the below snippet is used to check the functionality of "objects" in Django
class StudentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted = False)      

class Student(models.Model):
    Department = models.ForeignKey(Department, related_name="depart", on_delete=models.CASCADE)
    student_id = models.OneToOneField(studentID, related_name="studentid", on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField(unique=True)
    student_age = models.IntegerField(default=18)
    student_address = models.TextField()
    is_deleted = models.BooleanField(default = False)

# the below snippet is used to check the functionality of "objects" in Django
    objects = StudentManager()
    admin_objects = models.Manager()
    # Till here

    def __str__(self) -> str:
        return self.student_name
    
    class Meta:
        ordering = ["student_name"]
        verbose_name = "student"
    
        


class Subject(models.Model):
    subject_name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.subject_name


class SubjectMarks(models.Model):
    student = models.ForeignKey(Student, related_name="studentmarks", on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    subjectmarks = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.student.student_name}, {self.subject.subject_name}"
    
    class Meta:
        unique_together = ["student", "subject"]

class Reportcard(models.Model):
    student = models.ForeignKey(Student, related_name="student_rank", on_delete=models.CASCADE)        
    student_rank = models.IntegerField()
    result_date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.student.student_name}"

    class Meta:
        unique_together = ["student_rank","result_date"]
    
