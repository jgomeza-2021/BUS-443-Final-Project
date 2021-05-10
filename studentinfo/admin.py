from django.contrib import admin
from studentinfo.models import CourseDetails, StudentDetails, StudentEnrollment


# Register your models here.
admin.site.register(CourseDetails)
admin.site.register(StudentDetails)
admin.site.register(StudentEnrollment)