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
def questionnaire_edit(request,id) :
    question_list = models.Question.objects.filter(questionnaire__id=id)
    return render(request,"questionnaire_edit.html",{"question_list":question_list})