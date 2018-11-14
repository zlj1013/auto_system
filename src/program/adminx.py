# -*- coding: utf-8 -*-
#from program.apps import ProgramConfig
#导入xamin模块
import xadmin
#导入School表
from program.models import Course,Program
from xadmin import views
#创建注册类
class CourseAdmin(object):
    #可以是列表[],也可以是元组()，但使用元组只有一个字段是一定要加逗号
    list_display=['name',]
    #搜索框字段搜索配置
    search_fields=['name',]
    #筛选功能下拉选项字段设置
    list_filter=['name',]
    #每页显示多少个
    list_per_page=20
    #图标配置
    #model_icon='fa fa-user-plus'
    #显示详情
    show_detail_fields=['name']
    #数据刷新时间
    refresh_times=[120]

xadmin.site.register(Course, CourseAdmin)

class ProgramAdmin(object):
    #可以是列表[],也可以是元组()，但使用元组只有一个字段是一定要加逗号
    list_display=['pro_name',"pro_stype","story_num"]
    #搜索框字段搜索配置
    search_fields=['pro_name',]
    #筛选功能下拉选项字段设置
    list_filter=['pro_name',]
    #每页显示多少个
    list_per_page=20
    #图标配置
    #model_icon='fa fa-user-plus'
    #显示详情
    show_detail_fields=['pro_name']
    #数据刷新时间
    refresh_times=[120]

xadmin.site.register(Program, ProgramAdmin)


#基础设置
class GlobalSetting(object):
    #页头
    site_title="质量管理系统"
    #页脚
    site_footer="2011-2018优信.All Rights Reserved"
    #左侧菜单折叠样式
    menu_style="accordion"
    #设置左侧菜单图标
    global_search_models=[Program]
    global_models_icon={
        Program: "fa fa-user"
    }
xadmin.site.register(views.CommAdminView,GlobalSetting)

class BaseSetting(object):
    '''
    主题样式多样化
    '''
    enable_themes=True
    use_bootswatch=True

xadmin.site.register(views.BaseAdminView,BaseSetting)



