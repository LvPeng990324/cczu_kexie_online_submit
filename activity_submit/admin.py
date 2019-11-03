from django.contrib import admin
from .models import Student, SystemControl, Activity


@admin.register(SystemControl)
class SystemControlInformation(admin.ModelAdmin):
    pass


@admin.register(Activity)
class ActivityInformation(admin.ModelAdmin):
    pass


@admin.register(Student)
class StudentInformation(admin.ModelAdmin):
    list_display = ('name', 'stu_id', 'class_num', 'academy', 'qq_num', 'phone', 'team_id', 'is_leader', 'submit_time', )
    list_filter = ('class_num', 'academy', 'is_leader', )
    search_fields = ('name', 'stu_id', 'class_num', 'academy', 'qq_num', 'phone', 'team_id', 'is_leader', 'submit_time', )