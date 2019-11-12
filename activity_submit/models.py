from django.db import models


# 系统控制
class SystemControl(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='调控器id(不要动这个！)')
    can_submit = models.BooleanField(default=False, verbose_name='是否可以报名')
    team_size = models.IntegerField(verbose_name='组队规模')

    def __str__(self):
        return '系统控制(不要删除与添加)'

    class Meta:
        verbose_name_plural = '系统控制'
        verbose_name = '系统控制'


# 活动信息
class Activity(models.Model):
    name = models.CharField(max_length=50, primary_key=True, verbose_name='活动名称')
    introduction = models.TextField(verbose_name='活动介绍')
    title = models.CharField(max_length=50, verbose_name='报名表标题')
    context = models.TextField(verbose_name='报名表说明')
    qq_QRcode = models.ImageField(upload_to='QRcode', verbose_name='群二维码')
    qq_num = models.CharField(max_length=20, verbose_name='群号码')
    background_img = models.ImageField(upload_to='background_img', verbose_name='背景图')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '活动信息'
        verbose_name = '活动信息'


# 参赛者
class Student(models.Model):
    name = models.CharField(max_length=10, verbose_name='姓名')
    stu_id = models.CharField(max_length=10, primary_key=True, verbose_name='学号')
    class_num = models.CharField(max_length=20, verbose_name='班级')
    academy = models.CharField(max_length=20, verbose_name='学院')
    qq_num = models.CharField(max_length=15, verbose_name='QQ号')
    phone = models.CharField(max_length=15, verbose_name='手机号')
    team_id = models.CharField(max_length=5, verbose_name='队伍号')
    is_leader = models.BooleanField(default=False, verbose_name='是否队长')
    submit_time = models.DateTimeField(auto_now_add=True, verbose_name='报名时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '参赛者'
        verbose_name = '参赛者'


# 学院专业
class AcademyClass(models.Model):
    academy = models.CharField(max_length=20, verbose_name='学院')
    class_name = models.CharField(max_length=20, primary_key=True, verbose_name='专业')

    def __str__(self):
        return self.class_name

    class Meta:
        verbose_name_plural = '学院专业'
        verbose_name = '学院专业'
