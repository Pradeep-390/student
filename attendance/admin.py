from django.contrib import admin
from .models import Attendance

# egister your models here.

class AttendanceAdmin(admin.ModelAdmin):

    list_display = (
        "student",
        "attendance_date",
        "status",

    )

    list_filter = (
        "status",
        "attendance_date",
    )
    
admin.site.register(Attendance,AttendanceAdmin)