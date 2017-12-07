from django.shortcuts import render,redirect,HttpResponse

from app01 import models

# 登录
def login(request) :
    if request.method == "GET":
        return render(request, 'login.html')
    else :
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = models.UserInfo.objects.filter(name=username,pwd=password).first()
        if not user :
            return render(request, 'login.html')
        return redirect("/index/")

# 主页
def index(request) :
    questionnaire_list = models.Questionnaire.objects.all()
    return render(request,"index.html",{"questionnaire_list":questionnaire_list})

# 编辑问卷
from app01 import forms
# def questionnaire_edit(request,id) :
#     question_list = models.Question.objects.filter(questionnaire__id=id)
#     from_list = []
#     for question in question_list :
#         obj = forms.QuestionNaire(initial={"caption":question.caption,"tp":question.tp})
#         from_list.append(obj)
#     return render(request,"questionnaire_edit.html",{"from_list":from_list})
def questionnaire_edit(request,id) :
    def inner():
        que_list = models.Question.objects.filter(questionnaire__id=id)
        if not que_list:
            # 新创建的问卷，其中还么有创建问题
            form = forms.QuestionModelForm()
            yield {'form': form, 'obj': None, 'option_class': 'hide', 'options': None}
        else:
            # 含问题的问卷
            for que in que_list:
                form = forms.QuestionModelForm(instance=que)
                temp = {'form': form, 'obj': que, 'option_class': 'hide', 'options': None}
                if que.tp == 2:
                    temp['option_class'] = ''
                    # 获取当前问题的所有选项？que
                    def inner_loop(quee):
                        option_list = models.Option.objects.filter(qs=quee)
                        for v in option_list:
                            yield {'form':forms.OptionModelForm(instance=v), 'obj':v}
                    temp['options'] = inner_loop(que)
                yield temp
    return render(request, 'questionnaire_edit.html', {'form_list': inner(),"id":int(id)})

# 保存问卷
def question_save(request,nid) :
    import json
    lists = json.loads(request.body)
    print(lists)
    ids = []
    for lts in lists :
        question_obj = models.Question.objects.filter(id=lts.get('pid'))
        if question_obj :
            models.Question.objects.update(id=lts.get('pid'),caption=lts.get('caption'),tp=int(lts.get('type')))
        else :
            models.Question.objects.create(id=lts.get('pid'),caption=lts.get('caption'),tp=int(lts.get('type')),questionnaire_id=nid)
        ids.append(lts.get('pid'))
    question_list = models.Question.objects.filter(questionnaire_id=nid)
    for question_obj in question_list :
        if not question_obj.id in ids :
            question_obj.delete()
    # print(dicts.get('pid'))
    return HttpResponse("ok")

'''
[
    {'pid': '1', 'caption': '多好', 'type': '1', 'options': []}, 
    {'pid': '2', 'caption': '多帅', 'type': '2', 'options': 
        [
            {'id': '1', 'title': 'A.帅极了', 'val': '10'}, 
            {'id': '2', 'title': 'B.很帅', 'val': '9'}, 
            {'id': '3', 'title': 'C.帅', 'val': '8'}]}, 
    {'pid': '3', 'caption': '哪帅', 'type': '3', 'options': []}
]
'''
