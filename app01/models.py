from django.db import models

class UserInfo(models.Model):
    """
    员工表
    """
    name = models.CharField(verbose_name='姓名',max_length=32)
    pwd = models.CharField(verbose_name='密码',max_length=32)

class ClassList(models.Model):
    """
    班级表
    """
    title = models.CharField(verbose_name='班级',max_length=32)

class Student(models.Model):
    """
    学生表
    """
    user = models.CharField(verbose_name='姓名',max_length=32)
    pwd = models.CharField(verbose_name='密码',max_length=32)
    cls = models.ForeignKey(verbose_name='所属班级',to=ClassList)

class Questionnaire(models.Model):
    """
    问卷表
    """
    title = models.CharField(verbose_name='问卷名',max_length=64)
    cls = models.ForeignKey(verbose_name='所属班级',to=ClassList)
    creator = models.ForeignKey(verbose_name='创建人',to=UserInfo)

class Question(models.Model):
    """
    问题
    """
    caption = models.CharField(verbose_name='问题',max_length=64)
    question_types = (
        (1,'打分'),
        (2,'单选'),
        (3,'评价'),
    )
    tp = models.IntegerField(verbose_name='类型',choices=question_types)
    questionnaire = models.ManyToManyField(verbose_name='所属问卷',to=Questionnaire)

class Option(models.Model):
    """
    单选题的选项
    """
    name = models.CharField(verbose_name='选项名称',max_length=32)
    score = models.IntegerField(verbose_name='选项对应的分值')
    qs = models.ForeignKey(verbose_name='所属问题',to=Question)

class Answer(models.Model):
    """
    回答
    """
    stu = models.ForeignKey(verbose_name='回答学生',to=Student)
    question = models.ForeignKey(verbose_name='回答问题',to=Question)

    option = models.ForeignKey(verbose_name='单选',to="Option",null=True,blank=True)
    val = models.IntegerField(verbose_name='打分',null=True,blank=True)
    content = models.CharField(verbose_name='建议',max_length=255,null=True,blank=True)
