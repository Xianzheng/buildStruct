from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from .tools import getmodelfield, loadData, getHeader
from .models import *
from .forms import *
import sys
exclude = ['username','email','is_staff','last_login','password','last_name','date_joined','is_active','is_superuser']
@login_required(login_url="/acount/login/")
def levelOne_view(request):
    #得到表的第一个obj
    obj = LevelOne.objects.get(id = 1)
    #传入obj的字典格式obj.__dict__函数getheader得到表的第二项到最后一项
    #header exe： ['年度', '厂区名'],['月份', '用水量', '金额1', '用电量', '金额2']
    cs = getmodelfield('app', 'LevelOne',exclude)
    header = getHeader(obj.__dict__,start = 1, end = len(obj.__dict__) -1,cs = cs)
    header1 = getHeader(obj.__dict__,start = 2, end = (len(obj.__dict__)),cs = None)
    # print(header)
    #render style
    width = [200,250]
    #render到那个template
    renderFile = 'renderTable1.html' 
    #render header内容
    headerAndWidth = zip(header,width)
    #得到表的value
    objLst = LevelOne.objects.all()
    #遍历所有表的所有信息填入进空的lst中
    totalData = loadData(objLst, header1)
    # print('line28',totalData)

    #返回渲染template
    return render(request,renderFile,{'modelName':'LevelOne',
                'headerAndWidth':headerAndWidth,
                'totalData':totalData,'status':0,
                'tableName':'厂区表','tableId':0,
                'goback':'/logout/','nextLayout':'levelTwo'})

@login_required(login_url="/acount/login/")
def levelTwo_view(request,tableId):
    bindkey = LevelOne.objects.get(id = tableId)
    try:
        bindkey = LevelOne.objects.get(id = tableId)
        #一般情況一個表會有很多行所以要用filter,用get會報錯
        #header只用第一行的數據就可以得到,包括轉verbose_name的
        objLst = LevelTwo.objects.filter(bind = bindkey) 
        obj = objLst[0]
        cs = getmodelfield('app', 'LevelTwo',exclude)
        # cs look like {'id': 'id', '月份': '月份', '用水量': '用水量(m3)', '金额1': '金额(元)', '用电量': '用水量(kw.h)', '金额2': '金额(元)', 'bind': 'bind'}
        header = getHeader(obj.__dict__,start = 1, end = (len(obj.__dict__) - 1),cs = cs)
        # print(53,header)
        header1 = getHeader(obj.__dict__,start = 2, end = (len(obj.__dict__) - 1),cs = None)
        # header1 是models原生attribute名，header是轉換過的verbose_name
        #render style
        width = [100,100,100,100,100,100]
        renderFile = 'renderTable1.html' 
        headerAndWidth = zip(header,width)
        totalData = loadData(objLst, header1)
        # print('line 65',totalData)
        return render(request,renderFile,
                    {'headerAndWidth':headerAndWidth,
                    'totalData':totalData,'status':0,
                    'tableId':tableId,'tableName':'分厂区',
                    'modelName':'LevelTwo','goback':'/app/levelOne',
                    'nextLayout':'levelThree'})
    except:
        renderFile = 'renderTable1.html'  
        return render(request,renderFile,
                    {'headerAndWidth':[],
                    'totalData':[],'status':0,
                    'tableId':tableId,'tableName':'',
                    'modelName':'LevelTwo','goback':'levelOne',
                    'nextLayout':'levelThree'}) 

@login_required(login_url="/acount/login/")
def levelThree_view(request,tableId):
    bindkey = LevelTwo.objects.get(id = tableId)
    try:
        bindkey = LevelTwo.objects.get(id = tableId)
        #一般情況一個表會有很多行所以要用filter,用get會報錯
        #header只用第一行的數據就可以得到,包括轉verbose_name的
        objLst = LevelThree.objects.filter(bind = bindkey) 
        obj = objLst[0]
        cs = getmodelfield('app', 'LevelThree',exclude)
        # cs look like {'id': 'id', '月份': '月份', '用水量': '用水量(m3)', '金额1': '金额(元)', '用电量': '用水量(kw.h)', '金额2': '金额(元)', 'bind': 'bind'}
        header = getHeader(obj.__dict__,start = 1, end = (len(obj.__dict__) - 1),cs = cs)
        # print(53,header)
        header1 = getHeader(obj.__dict__,start = 2, end = (len(obj.__dict__) - 1),cs = None)
        # header1 是models原生attribute名，header是轉換過的verbose_name
        #render style
        print(header)
        width = [100,100,100,100,100,100]
        renderFile = 'renderTable1.html' 
        headerAndWidth = zip(header,width)
        totalData = loadData(objLst, header1)
        # print('line 65',totalData)
        return render(request,renderFile,
                    {'headerAndWidth':headerAndWidth,
                    'totalData':totalData,'status':0,
                    'tableId':tableId,'tableName':'分厂区',
                    'modelName':'LevelThree','goback':'/app/levelTwo/1',
                    'nextLayout':'levelFour'})
    except:
        renderFile = 'renderTable1.html'  
        print('LevelThree Error')
        return render(request,renderFile,
                    {'headerAndWidth':[],
                    'totalData':[],'status':0,
                    'tableId':tableId,'tableName':'',
                    'modelName':'LevelThree','goback':'/app/levelTwo/1',
                    'nextLayout':'levelFour'}) 

@login_required(login_url="/acount/login/")
def levelFour_view(request,tableId):
    bindkey = LevelThree.objects.get(id = tableId)
    try:
        bindkey = LevelThree.objects.get(id = tableId)
        #一般情況一個表會有很多行所以要用filter,用get會報錯
        #header只用第一行的數據就可以得到,包括轉verbose_name的
        objLst = LevelFour.objects.filter(bind = bindkey) 
        obj = objLst[0]
        cs = getmodelfield('app', 'LevelFour',exclude)
        # cs look like {'id': 'id', '月份': '月份', '用水量': '用水量(m3)', '金额1': '金额(元)', '用电量': '用水量(kw.h)', '金额2': '金额(元)', 'bind': 'bind'}
        header = getHeader(obj.__dict__,start = 1, end = (len(obj.__dict__) - 1),cs = cs)
        # print(53,header)
        header1 = getHeader(obj.__dict__,start = 2, end = (len(obj.__dict__) - 1),cs = None)
        # header1 是models原生attribute名，header是轉換過的verbose_name
        #render style
        print(header)
        width = [250,300,300]
        renderFile = 'renderTable1.html' 
        headerAndWidth = zip(header,width)
        totalData = loadData(objLst, header1)
        # print('line 65',totalData)
        return render(request,renderFile,
                    {'headerAndWidth':headerAndWidth,
                    'totalData':totalData,'status':0,
                    'tableId':tableId,'tableName':'分厂区',
                    'modelName':'LevelFour','goback':'/app/levelThree/1',
                    'nextLayout':'levelFive'})
    except:
        renderFile = 'renderTable1.html'  
        print('LevelThree Error')
        return render(request,renderFile,
                    {'headerAndWidth':[],
                    'totalData':[],'status':0,
                    'tableId':tableId,'tableName':'',
                    'modelName':'LevelFour','goback':'/app/levelThree/1',
                    'nextLayout':'levelFive'}) 

@login_required(login_url="/acount/login/")
def levelFive_view(request,tableId):
    bindkey = LevelFour.objects.get(id = tableId)
    try:
        bindkey = LevelFour.objects.get(id = tableId)
        #一般情況一個表會有很多行所以要用filter,用get會報錯
        #header只用第一行的數據就可以得到,包括轉verbose_name的
        objLst = LevelFive.objects.filter(bind = bindkey) 
        obj = objLst[0]
        cs = getmodelfield('app', 'LevelFive',exclude)
        # cs look like {'id': 'id', '月份': '月份', '用水量': '用水量(m3)', '金额1': '金额(元)', '用电量': '用水量(kw.h)', '金额2': '金额(元)', 'bind': 'bind'}
        header = getHeader(obj.__dict__,start = 1, end = (len(obj.__dict__) - 1),cs = cs)
        # print(53,header)
        header1 = getHeader(obj.__dict__,start = 2, end = (len(obj.__dict__) - 1),cs = None)
        # header1 是models原生attribute名，header是轉換過的verbose_name
        #render style
        print(header)
        width = [100,100,100,100,100,100]
        renderFile = 'renderTable1.html' 
        headerAndWidth = zip(header,width)
        totalData = loadData(objLst, header1)
        # print('line 65',totalData)
        return render(request,renderFile,
                    {'headerAndWidth':headerAndWidth,
                    'totalData':totalData,'status':1,
                    'tableId':tableId,'tableName':'分厂区',
                    'modelName':'LevelFive','goback':'/app/levelFour/1',
                    'nextLayout':'levelFour'})
    except:
        renderFile = 'renderTable1.html'  
        print('LevelThree Error')
        return render(request,renderFile,
                    {'headerAndWidth':[],
                    'totalData':[],'status':1,
                    'tableId':tableId,'tableName':'',
                    'modelName':'LevelFive','goback':'/app/levelThree/1',
                    'nextLayout':'levelFour'}) 

@login_required(login_url="/login/")
def addSubTable_view(request,tableId,tableModel):
    print('tableId is ',tableId)
    print('tableModel is',tableModel,type(tableModel))
    path = request.path
    modelName = path.split('/')[-1]
    formName = modelName +'_Form'
    form = globals()[formName]
    model = globals()[modelName]
    print(tableId)
    if request.method == 'POST':
        form = form(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            if tableId == '0':# 如果tableId等于0意味着根表，没有foreign key
                pass
            else:
                # instance.bind = model.objects.get(id = tableId)
                if tableModel == 'LevelTwo':
                    instance.bind = LevelOne.objects.get(id = tableId)
                if tableModel == 'LevelThree':
                    instance.bind = LevelTwo.objects.get(id = tableId)
                if tableModel == 'LevelFour':
                    instance.bind = LevelThree.objects.get(id = tableId)
                if tableModel == 'LevelFive':
                    instance.bind = LevelFour.objects.get(id = tableId)
            instance.save()
            
            rd = tableModel[0].lower() + tableModel[1:]
            return redirect('/app/'+rd+'/'+tableId)
    else:

        path = request.path
        modelName = path.split('/')[-1]
        formName = modelName +'_Form'
        form = globals()[formName]
        title = '添加厂区'
        rd = tableModel[0].lower() + tableModel[1:]
        print(rd)
        goback = '/app/'+rd+'/'+tableId

    return render(request,'form.html',{'form':form,
    'tableName':title,'goback':goback})
    
    return HttpResponse(1)
'''
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
'''
