from django.shortcuts import render, redirect, HttpResponse
from.models import Activity, Student, SystemControl
from random import randint


# 活动报名入口
def index(response):
    if response.method == 'POST':
        # 从首页获得成员身份
        teammate = response.POST.get('teammate')
        # 判断成员身份
        if teammate == '队员':
            return redirect('submit_form', teammate)
        elif teammate == '队长':
            return redirect('submit_form', teammate)
        else:
            # 基本上不可能出现的情况，除非出现了未知错误
            return HttpResponse('发生未知错误，请重试！或者联系管理员，提交错误码:1')
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
def submit_form(response, teammate):
    if response.method == 'POST':
        # 将信息从前端拿到
        name = response.POST.get('name')
        class_num = response.POST.get('class_num')
        academy = response.POST.get('academy')
        stu_id = response.POST.get('stu_id')
        phone = response.POST.get('phone')
        qq_num = response.POST.get('qq_num')
        # 判断这个学号是否已报名
        # 从数据库中查询此学号
        if len(Student.objects.filter(stu_id=stu_id)) > 0:
            # 如果已报名返回你已报名，以及报名信息，提示不要重复提交，如需修改信息联系管理员
            # 尝试从数据库中取出此人信息
            try:
                data = Student.objects.get(stu_id=stu_id)
            except:
                # 返回数据库读取错误
                return HttpResponse('数据库读取错误，重试或联系管理员，提交错误码：5')
            # 尝试取出队员姓名
            try:
                teammate_names = Student.objects.filter(team_id=data.team_id)
            except:
                # 返回数据库读取错误
                return HttpResponse('数据库读取错误，重试或联系管理员，提交错误码：6')
            # 打包报名信息以及队员姓名
            context = {
                'name': name,
                'class_num': data.class_num,
                'academy': data.academy,
                'stu_id': data.stu_id,
                'phone': data.phone,
                'qq_num': data.qq_num,
                'team_id': data.team_id,
                'is_leader': data.is_leader,
                'teammate_names': teammate_names,
            }
            # 引导前端页面
            return render(response, 'error_multiple_submit.html', context=context)

        else:
            # 没有报名则过
            pass

        # 如果是队长，则分配队伍号，队员就从前端获得
        # 设置是否为对长属性
        if teammate == '队长':
            # 随机生成1-10000的队伍号
            team_id = randint(1, 10000)
            # 检查队伍号是否与数据库中的重复
            # 重复就重新生成，直到不重复为止
            while len(Student.objects.filter(team_id=team_id)) != 0:
                team_id = randint(1, 10000)
            # 设置是否为队长属性
            is_leader = True
        elif teammate == '队员':
            # 取到队伍号
            team_id = response.POST.get('team_id')
            # 查询数据库中此队伍号
            # 如果队伍号不存在返回队伍号不存在错误
            # 如果队伍号数量超过设置的组队规模，返回此队已满错误
            num_team_id = len(Student.objects.filter(team_id=team_id))
            if num_team_id == 0:
                # 打包队伍号不存在错误并返回前端
                context = {
                    'error_message': '队伍{}不存在!'.format(team_id),
                    'teammate': teammate,
                }
                return render(response, 'submit_form.html', context=context)
            if num_team_id >= SystemControl.objects.get(id=1).team_size:
                # 打包此队已满错误并返回前端
                context = {
                    'error_message': '队伍{}已满!'.format(team_id),
                    'teammate': teammate,
                }
                return render(response, 'submit_form.html', context=context)
            else:
                # 没问题就设置是否为队长属性
                is_leader = False
        else:
            # 基本上不可能出现的情况，除非出现了未知错误
            return HttpResponse('发生未知错误，请重试！或者联系管理员，提交错误码:2')
        # 存入数据库
        try:
            # 存入数据库
            Student.objects.get_or_create(
                name=name,
                class_num=class_num,
                academy=academy,
                stu_id=stu_id,
                phone=phone,
                qq_num=qq_num,
                team_id=team_id,
                is_leader=is_leader,
            )
        except:
            # 返回数据库写入错误
            return HttpResponse('数据库写入错误！重试或联系管理员，提交错误码：3')
        # 从数据库中取出队员名字
        # 打包报名信息
        # 将信息传入前端
        # 尝试从数据库中取出队员信息
        try:
            teammate_names = Student.objects.filter(team_id=team_id)
        except:
            # 返回数据库读取错误
            return HttpResponse('数据库读取错误，但是报名信息已成功提交，联系管理员以确认你的信息，提交错误码：4')
        # 打包报名信息以及队员名字
        context = {
            'name': name,
            'class_num': class_num,
            'academy': academy,
            'stu_id': stu_id,
            'phone': phone,
            'qq_num': qq_num,
            'team_id': team_id,
            'is_leader': is_leader,
            'teammate_names': teammate_names,
        }
        # 传参并引导前端页面
        return render(response, 'success.html', context=context)
    else:
        # 打包成员信息并引导信息表页面
        context = {
            'teammate': teammate,
        }
        return render(response, 'submit_form.html', context=context)
