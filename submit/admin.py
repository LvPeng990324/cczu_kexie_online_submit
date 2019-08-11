from django.contrib import admin
from .models import NewPerson, KeXiePerson
from .csvMaker import export_as_csv_action

# Register your models here.


class NewPersonProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'sex', 'class_num', 'school', 'department', 'phone', 'qq_num', 'changeable')
    list_filter = ('department', 'class_num', 'school', 'changeable', 'sex')
    search_fields = ('name', 'sex', 'class_num', 'school' 'department', 'phone', 'qq_num', 'changeable')
    actions = [export_as_csv_action('导出表格', fields=['name', 'sex', 'class_num', 'school' 'department', 'phone', 'qq_num', 'changeable'])]


class KeXiePersonProfileAdmin(admin.ModelAdmin):
    list_display = ('kexie_id', 'name', 'stu_id', 'sex', 'school', 'department', 'department_job', 'class_num', 'academy', 'qq_num', 'phone', 'dorm', 'year')
    list_filter = ('department', 'sex', 'school', 'department', 'department_job', 'academy', 'year')
    search_fields = ('kexie_id', 'name', 'stu_id', 'sex', 'school', 'department', 'department_job', 'class_num', 'academy', 'qq_num', 'phone', 'dorm', 'year')


admin.site.register(NewPerson, NewPersonProfileAdmin)
admin.site.register(KeXiePerson, KeXiePersonProfileAdmin)

