from django.shortcuts import render, HttpResponse
from .models import NewPerson, KeXiePerson
from django.db.utils import IntegrityError

# Create your views here.


# 科协招新
def new_person_request(request):
    return render(request, 'new_person.html')


# 科协正式人员信息统计
def kexie_person_request(request):
    return render(request, 'kexie_person.html')


def new_person_submit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        sex = request.POST.get('sex')
        stu_id = request.POST.get('stu_id')
        class_num = request.POST.get('class_num')
        school = request.POST.get('school')
        department = request.POST.get('department')
        phone = request.POST.get('phone')
        qq_num = request.POST.get('qq_num')
        changeable = request.POST.get('changeable')

        try:
            NewPerson.objects.get_or_create(
                name=name,
                sex=sex,
                stu_id=stu_id,
                class_num=class_num,
                school=school,
                department=department,
                phone=phone,
                qq_num=qq_num,
                changeable=changeable
            )
        except IntegrityError as e:
            return HttpResponse('提交出错，此学号已有记录，且你提交的内容与记录内容有不同处，重复提交无效。如需修改信息请联系我们')
        '''
        print(name)
        print(sex)
        print(stu_id)
        print(class_num)
        print(school)
        print(department)
        print(phone)
        print(qq_num)
        print(changeable)
        '''
        return render(request, 'thanks.html')
    else:
        return render(request, 'new_person.html')


def submit(request, name, sex, class_num, school, stu_id, phone, qq_num, department, changeable):
    NewPerson.objects.get_or_create(
        name=name,
        sex=sex,
        stu_id=stu_id,
        class_num=class_num,
        school=school,
        department=department,
        phone=phone,
        qq_num=qq_num,
        changeable=changeable
    )
    '''
    print('姓名：', name)
    print('性别：', sex)
    print('班级：', class_num)
    print('校区：', school)
    print('学号：', stu_id)
    print('手机号：', phone)
    print('QQ号：', qq_num)
    print('想去的部门：', department)
    print('是否服从调剂：', changeable)
    '''
    return HttpResponse('提交成功！')


def kexie_person_submit(request):
    if request.method == 'POST':
        # kexie_id = request.POST.get('kexie_id')
        name = request.POST.get('name')
        stu_id = request.POST.get('stu_id')
        sex = request.POST.get('sex')
        school = request.POST.get('school')
        department = request.POST.get('department')
        department_job = request.POST.get('department_job')
        class_num = request.POST.get('class_num')
        academy = request.POST.get('academy')
        qq_num = request.POST.get('qq_num')
        phone = request.POST.get('phone')
        dorm = request.POST.get('dorm')
        # year = request.POST.get('year')

        # 从学号提取入学年份
        year = '20' + stu_id[:2]

        # 生成编号前段，规则：年份+校区+部门+部门序号（后期由管理员分配部门序号，这里仅自动加上XX占位）
        # 白云0、武进1、西太湖2
        # 办公室0、科创1、外联2、网信3、宣传4、项管5
        dic_school = {
            '白云校区': '0',
            '武进校区': '1',
            '西太湖校区': '2',
        }
        dic_department = {
            '办公室': '0',
            '科创部': '1',
            '外联部': '2',
            '网信部': '3',
            '宣传部': '4',
            '项管部': '5',
        }
        kexie_id = stu_id[:2] + dic_school[school] + dic_department[department] + 'XX'
        '''
        print(kexie_id)
        print(name)
        print(stu_id)
        print(sex)
        print(school)
        print(department)
        print(department_job)
        print(class_num)
        print(academy)
        print(qq_num)
        print(phone)
        print(dorm)
        print(year)
        '''
        try:
            KeXiePerson.objects.get_or_create(
                kexie_id=kexie_id,
                name=name,
                stu_id=stu_id,
                sex=sex,
                school=school,
                department=department,
                department_job=department_job,
                class_num=class_num,
                academy=academy,
                qq_num=qq_num,
                phone=phone,
                dorm=dorm,
                year=year
            )
        except IntegrityError as e:
            return HttpResponse('提交出错，此学号已有记录，且你提交的内容与记录内容有不同处，重复提交无效。如需修改信息请联系我们')

        return render(request, 'thanks.html')
    else:
        return render(request, 'kexie_person.html')


