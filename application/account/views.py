from django.shortcuts import render,redirect

from django.contrib.auth import login,logout

from django.contrib.auth.models import User, Group

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm

from django.http.response import HttpResponse

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
import datetime
# Create your views here.
def writeToLog(request,string):
    with open('Log.txt','a',encoding= 'utf-8') as f:
        f.write(string)
        f.write('\n')

def getCurrentTime():
    now_time = datetime.datetime.now()
    str_time = datetime.datetime.strftime(now_time,'%Y-%m-%d %H:%M:%S')
    return str_time

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            # return redirect('/dogInfo_list/')
            user = form.get_user()
            login(request,user)

            # if 'next' in request.POST:
            #     return redirect(request.POST.get('next'))
            # else:
            ip = get_client_ip(request)
            print('用户 {} ip {} 登陆'.format(request.user.first_name,ip))
            string = '用户 {} ip {} 时间 {} 登陆 '.format(request.user.first_name,ip,getCurrentTime())
            writeToLog(request,string)
            return redirect('/testapp/table1')#这里必须要127.0.0.1后的完整url
    else:
        form = AuthenticationForm()
        title = '动能消耗统计'
        background = 'image/download.jfif'
    return render(request,"login.html",{'form':form,'title':title,'backgroundImage':background})

def logout_view(request):
    
        if request.user:
            logout(request)
        return redirect('/login/')

def changePass_view(request):

    if request.method == 'POST':
        
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            # print('it is valid')
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            # messages.success(request, 'Your password was successfully updated!')
            return redirect('/index/')
        else:
            # print('it is not valid')
            return render(request, 'changeError.html')
    
    else:
        form = PasswordChangeForm(request.user)
        return render(request, 'changePass.html',{"form":form})

