from django.shortcuts import render, redirect
from.models import Activity, Student, SystemControl


# 活动报名入口
def index(response):
    if response.method == 'POST':
        pass
    else:
        # 从数据库中取出活动信息并展示到主页
        context = {
            'name': Activity.objects.all()[0].name,
            'introduction': Activity.objects.all()[0].introduction,
            'qq_num': Activity.objects.all()[0].qq_num,
            'qq_QRcode': Activity.objects.all()[0].qq_QRcode,
        }
        return render(response, 'index.html', context=context)


# 报名表
def submit_form(response):
    if response.method == 'POST':
        pass
    else:
        return redirect('/activity_submit/')
