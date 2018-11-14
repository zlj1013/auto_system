# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime
# Create your models here.
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
    pro=(("1","金融中心"),("2","优信二手车"),("3","优信拍"))
    pro_name=models.CharField(choices=pro,max_length=50,verbose_name='部门')
    pro_stype=models.CharField(max_length=100,verbose_name='项目名')
    story_num=models.IntegerField(default=0,verbose_name="上线需求")
    add_time=models.DateTimeField(default=datetime.now,verbose_name='开始时间')
    #add_time=models.DateTimeField(verbose_name='结束时间')

    class Meta:
        verbose_name='项目管理'#后台显示的名称
        verbose_name_plural=verbose_name# 后台显示的表名复数  英语复数是加s

    def __str__(self):
        return self.pro_name