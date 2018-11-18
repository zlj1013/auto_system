from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect  #这三个模块为常用模块
# Create your views here.

def gologin(request):
    return render(request, 'uxin_login.html')
def login(request):
    if request.method == 'POST':            #判断是否为post提交方式
        #username = request.POST.get('username', '')   #通过post.get()方法获取输入的用户名及密码
        #password =request.POST.get('password', '')

        if True:
        #if username == 'zhulijuan1' and password == '123456':  #判断用户名及密码是否正确
            return HttpResponseRedirect('/index/')     #如果正确，（这里调用另一个函数，实现登陆成功页面独立，使用HttpResponseRedirect()方法实现
        else:
            return render(request,'uxin_login.html',{'error':'username or password eror'})#不正确，通过render(request,"index.html")方法在error标签处显示错误提示

def index(request):               #该函数定义的是成功页面的提示页面
    return render(request,"index.html") #在上面的函数判断用户名密码正确后在显示该页面，指定到index.html,切换到一个新的html页面

def logout(request):
    return render(request, 'uxin_login.html')