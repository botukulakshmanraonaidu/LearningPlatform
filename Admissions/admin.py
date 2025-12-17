from django.contrib import admin
from Admissions.models import addadmissions

# Register your models here.

class addadmissionsadmin(admin.ModelAdmin):
    list_display = ['COURSE_CHOICES','student_name','father_name','dob','course_opted','Registration_fee']

admin.site.register(addadmissions,addadmissionsadmin)
