from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from .tools import getmodelfield, loadData, getHeader
from .models import *
from .forms import *

exclude = ['username','email','is_staff','last_login','password','last_name','date_joined','is_active','is_superuser']

# Create your views here.
@login_required(login_url="/account/login/")
def hello(request):
    return HttpResponse('hello')

@login_required(login_url="/acount/login/")
def index_view(request):
    #得到表的第一个obj
    obj = 厂区.objects.get(id = 1)
    #传入obj的字典格式obj.__dict__函数getheader得到表的第二项到最后一项
    #header exe： ['年度', '厂区名'],['月份', '用水量', '金额1', '用电量', '金额2']
    cs = getmodelfield('app', '厂区',exclude)
    header = getHeader(obj.__dict__,start = 1, end = len(obj.__dict__) -1,cs = cs)
    # print(header)
    #render style
    width = [200,250]
    #render到那个template
    renderFile = 'renderTable.html' 
    #render header内容
    headerAndWidth = zip(header,width)
    #得到表的value
    objLst = 厂区.objects.all()
    #遍历所有表的所有信息填入进空的lst中
    totalData = loadData(objLst, header)
    # print('line28',totalData)

    #返回渲染template
    return render(request,renderFile,
                {'headerAndWidth':headerAndWidth,
                'totalData':totalData,'status':0,
                'tableName':'廠區年度消耗表'})

@login_required(login_url="/acount/login/")
def tableDetail_view(request,tableId):
    bindkey = 厂区.objects.get(id = tableId)
    try:
        bindkey = 厂区.objects.get(id = tableId)
        #一般情況一個表會有很多行所以要用filter,用get會報錯
        #header只用第一行的數據就可以得到,包括轉verbose_name的
        objLst = 消耗.objects.filter(bind = bindkey) 
        obj = objLst[0]
        cs = getmodelfield('app', '消耗',exclude)
        # cs look like {'id': 'id', '月份': '月份', '用水量': '用水量(m3)', '金额1': '金额(元)', '用电量': '用水量(kw.h)', '金额2': '金额(元)', 'bind': 'bind'}
        header = getHeader(obj.__dict__,start = 1, end = (len(obj.__dict__) - 4),cs = cs)
        # print(53,header)
        header1 = getHeader(obj.__dict__,start = 2, end = (len(obj.__dict__) - 3),cs = None)
        # header1 是models原生attribute名，header是轉換過的verbose_name
        #render style
        width = [100,100,100,100,100,100]
        renderFile = 'renderTable.html' 
        headerAndWidth = zip(header,width)
        totalData = loadData(objLst, header1)
        # print('line 65',totalData)
        return render(request,renderFile,
                    {'headerAndWidth':headerAndWidth,
                    'totalData':totalData,'status':1,
                    'tableId':tableId,'tableName':obj})
    except:
        print('table view error')
        renderFile = 'renderTable.html'  
        return render(request,renderFile,
                    {'headerAndWidth':[],
                    'totalData':[],'status':1,
                    'tableId':tableId,'tableName':''}) 


@login_required(login_url="/acount/login/")
def updateRow_view(request,rowId,tableId):
    # print('更新id',rowId)
    obj = LevelFive.objects.get(id = rowId)
    if request.method == 'POST':
        form = LevelFive_Form(request.POST,instance = obj)
        if form.is_valid():
            form.save()
            return redirect("/app/levelFive/"+tableId)

    form = LevelFive_Form(instance = obj)
    title = '修改消耗表单'
    action = '/app/updateRow/'+rowId+'/'+tableId
    goback = '/app/analyze/'+tableId
    return render(request,'form.html',
    {'form':form,'tableName':title,
    'tableId':tableId,'action':action,'goback':goback})

@login_required(login_url="/login/")
def deleteRow_view(request,rowId,tableId):
    obj = LevelFive.objects.get(id = rowId)
    obj.delete()
    return redirect("/app/levelFive/"+tableId)

@login_required(login_url="/login/")
def addRow_view(request,tableId):
    if request.method == 'POST':
        form = 消耗表(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.bind = 厂区.objects.get(id = tableId)
            instance.save()
           
            return redirect('/app/tableDetail/'+tableId)
    else:
        form = 消耗表() # must come from .form.py
        title = '添加消耗'
        goback = '/app/tableDetail/'+tableId 
    return render(request,'form.html',{'form':form,
    'tableName':title,'goback':goback})

    