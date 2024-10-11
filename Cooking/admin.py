from django.contrib import admin
from Cooking.models import *
from django.db.models import Sum

# Register your models here.
admin.site.register(Recipeform)
admin.site.register(Department)
admin.site.register(studentID)
admin.site.register(Student)

admin.site.register(Subject)

class subjectMarksAdmin(admin.ModelAdmin):
    list_display = ["student", "subject", "subjectmarks"]

admin.site.register(SubjectMarks, subjectMarksAdmin)

class ReportcardAdmin(admin.ModelAdmin):
    list_display = ["student", "total_marks", "student_rank", "result_date"]
    ordering = ["student_rank"]
    def total_marks(self,obj):
        subject_marks = SubjectMarks.objects.filter(student = obj.student)
        marks_obj = subject_marks.aggregate(marks = Sum("subjectmarks"))
        return marks_obj["marks"]


admin.site.register(Reportcard, ReportcardAdmin)
