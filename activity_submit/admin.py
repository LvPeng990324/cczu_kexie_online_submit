from django.contrib import admin
from .models import Student, SystemControl, Activity, AcademyClass
from django.http import HttpResponse
import csv


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
    actions = ['export_as_csv']

    def export_as_csv(self, request, queryset):
        meta = self.model._meta  # 用于确定导出的文件名, 格式为: app名.模型类名
        field_names = [field.name for field in meta.fields]  # 所有属性名

        response = HttpResponse(content_type='text/csv')   # 指定响应内容类型
        response['Content-Disposition'] = f'attachment; filename={meta}.csv'
        response.charset = 'utf-8-sig'  # 可选, 修改编码为带BOM的utf-8格式(Excel打开不会有乱码)
        writer = csv.writer(response)
        writer.writerow(field_names)  # 将属性名写入csv
        for obj in queryset:  # 遍历要导出的对象列表
            row = writer.writerow([getattr(obj, field) for field in field_names])  # 将当前对象的各属性值写入csv
        return response
    export_as_csv.short_description = '表格形式导出所选内容'


@admin.register(AcademyClass)
class AcademyClassInformation(admin.ModelAdmin):
    list_display = ('class_name', 'academy', )
    list_filter = ('academy', 'class_name', )
    search_fields = ('academy', 'class_name', )
