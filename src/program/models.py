# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime
#from django.contrib.auth.models import AbstractUser

class Course(models.Model):
    '''
    学校表
    '''
    name=models.CharField(max_length=50,verbose_name='学校名字')
    address=models.CharField(max_length=100,verbose_name='学校地址')
    add_time=models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    class Meta:
        verbose_name='学校'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name
    
class Program(models.Model):
    '''
    项目表设计
    '''
    pro=(("1","对公金融"),("2","保险系统"),("3","养成快现"))
    depart=(("1","个贷金融"),("2","金融保险"))
    depart_name=models.CharField(choices=depart,max_length=50,verbose_name='部门')
    pro_name=models.CharField(choices=pro,max_length=50,verbose_name='项目名')
    primary_requirement=models.CharField(max_length=100,verbose_name='主要需求')
    special_requirement=models.CharField(max_length=200,verbose_name='具体需求')
    renew_starttime=models.DateField(verbose_name='需求评审时间', blank=True, null=True)
    plan_testtime=models.DateField(verbose_name='计划提测时间', blank=True, null=True)
    fact_testtime=models.DateField(verbose_name='实际提测时间', blank=True, null=True)
    plan_goline_time=models.DateField(verbose_name='计划上线时间', blank=True, null=True)
    fact_goline_time=models.DateField(verbose_name='实际上线时间', blank=True, null=True)
    tester_num=models.IntegerField(verbose_name="测试人力",blank=True, null=True)
    bug_num=models.IntegerField(verbose_name="bug数",blank=True, null=True)
    remark=models.CharField(max_length=100,verbose_name='备注',blank=True, null=True)
    add_time=models.DateTimeField(auto_now_add=True,verbose_name='添加时间')

    class Meta:
        #db_name="program"
        verbose_name='项目版本计划'#后台显示的名称
        verbose_name_plural=verbose_name# 后台显示的表名复数  英语复数是加s

    def __str__(self):
        return self.pro_name