from django.db import models

# Create your models here.

# 科协招新名单
class NewPerson(models.Model):
    name = models.CharField(max_length=10, verbose_name='姓名')
    sex = models.CharField(max_length=2, verbose_name='性别')
    stu_id = models.CharField(max_length=10, primary_key=True, verbose_name='学号')
    class_num = models.CharField(max_length=10, verbose_name='班级')
    school = models.CharField(max_length=10, verbose_name='校区')
    department = models.CharField(max_length=10, verbose_name='意向部门')
    phone = models.CharField(max_length=15, verbose_name='手机号')
    qq_num = models.CharField(max_length=15, verbose_name='QQ号')
    changeable = models.CharField(max_length=2, verbose_name='是否接受调剂')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '小萌新'
        verbose_name_plural = '小萌新名单'


# 科协正式人员信息统计
class KeXiePerson(models.Model):
    kexie_id = models.CharField(max_length=10, verbose_name='编号')
    name = models.CharField(max_length=10, verbose_name='姓名')
    stu_id = models.CharField(max_length=10, primary_key=True, verbose_name='学号')
    sex = models.CharField(max_length=2, verbose_name='性别')
    school = models.CharField(max_length=10, verbose_name='校区')
    department = models.CharField(max_length=10, verbose_name='部门')
    department_job = models.CharField(max_length=10, verbose_name='部门职务')
    class_num = models.CharField(max_length=10, verbose_name='班级')
    academy = models.CharField(max_length=20, verbose_name='学院')
    qq_num = models.CharField(max_length=15, verbose_name='QQ号')
    phone = models.CharField(max_length=15, verbose_name='手机号')
    dorm = models.CharField(max_length=15, verbose_name='宿舍')
    year = models.CharField(max_length=15, verbose_name='入学年份')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '科仔信息'
        verbose_name_plural = '科仔信息'

