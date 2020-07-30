'''
@Author: xyb
@Date: 2020-07-24 21:57:19
@LastEditTime: 2020-07-25 17:35:59
'''
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import re

# Create your views here.
from book.models import BookInfo, PeopleInfo, User

def login_page(request):
    if request.method == 'GET':
        return render(request, 'login.html', {'error': ''})
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == '' or password == '':
            return render(request, 'login.html', {'error': '请填写用户名和密码'})
        if username != '' and password != '':
            Acountinfo = User.objects.filter(username=username)
            for user in Acountinfo:
                if user.password == password:
                    User.is_login = True
                    User.login_name = user.username
                    return HttpResponseRedirect("/booklist.html/")
                if user.password != password:
                    return render(request, 'login.html', {'error': '密码错误'})
            if not Acountinfo:
                return render(request, 'login.html', {'error': '此用户不存在'})

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html', {'error': ''})
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        phonenum = request.POST.get('phonenum')
        if username == '' or password == '' or email == '':
            return render(request, 'register.html', {'error': '请将信息填写完整'})
        if username != '' and password != '' and email != '':
            #记得查重：已经存在的用户不能再注册
            Acountinfo = User.objects.filter(username=username)
            for user in Acountinfo:
                if user.username == '':
                    #验证邮箱的合法性
                    ret = re.match('\w{4,20}@(qq|163|126|gmail|outlook)\.com$', email)
                    if ret:
                        #将用户数据存入数据库
                        User.objects.create(
                            username=username,
                            password=password,
                            email=email,
                            phonenum=phonenum,)
                        User.is_login = True
                        User.login_name = username
                        return HttpResponse("/booklist.html/")
                    if not ret:
                        return render(request, 'register.html', {'error': '邮箱不合法'})
                if user.username != '':
                    return render(request, 'register.html', {'error': '该用户已经存在'})

def find_password(request):
    if request.method == 'GET':
        return render(request, 'find_password.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        if username == '' or email == '':
            return render(request, 'find_password.html', {'error': '请把信息填写完整'})
        if username != '' and email != '':
            Acountinfo = User.objects.filter(username=username)
            for user in Acountinfo:
                password = {'password': user.password}
                if user.username == username and user.email == email:
                    return render(request, 'find_password.html', password)
                if user.username != username or user.email != email:
                    return render(request, 'find_password.html', {'error': '邮箱与用户名不匹配'})

def booklist(request):
    #查询数据库书籍列表数据
    #books = BookInfo.objects.all()#只有名字
    books = [book.name for book in (BookInfo.objects.all())]
    peoples = PeopleInfo.objects.all()
    #print(peoples)
    #构造上下文
    content = {'books': books}
    #数据交给模板处理，处理完后通过视图响应给客户端
    return render(request, 'book/booklist.html', content)

def kobe(request):
    return render(request, 'kobe.html')