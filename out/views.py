
from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from .tools import getmodelfield, loadData, getHeader
from .models import *
from .forms import *
from pathlib import Path
import sys
exclude = ['username','email','is_staff','last_login','password','last_name','date_joined','is_active','is_superuser']

BASE_DIR = Path(__file__).resolve().parent
rootFilePath = str(BASE_DIR).split('\\')[-1]
        
@login_required(login_url="/acount/login/")
def table1_view(request):
    modelName = 'table1'
    nextModleName = 'table2'
    if nextModleName == '':
        nextModleName = modelName
    modelInstance = globals()[modelName]
    #得到表的第一个obj
    objLst = modelInstance.objects.all()
    try:
        obj = objLst[0]
        #传入obj的字典格式obj.__dict__函数getheader得到表的第二项到最后一项
        cs = getmodelfield(rootFilePath, modelName,exclude)
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
        objLst = modelInstance.objects.all()
        #遍历所有表的所有信息填入进空的lst中
        totalData = loadData(objLst, header1)
        # print('line28',totalData)

        #返回渲染template
        return render(request,renderFile,{'modelName':modelName,
                    'headerAndWidth':headerAndWidth,
                    'totalData':totalData,'status':0,
                    'tableName':'厂区表','tableId':0,
                    'goback':'/logout/','nextLayout':'/'+rootFilePath+'/'+nextModleName})
    except:
        renderFile = 'renderTable1.html'  
        return render(request,renderFile,{'modelName':modelName,
                    'headerAndWidth':'',
                    'totalData':'','status':0,
                    'tableName':'厂区表','tableId':0,
                    'goback':'/logout/','nextLayout':'/'+rootFilePath+'/'+nextModleName})
                
@login_required(login_url="/acount/login/")
def table2_view(request,tableId):
    rootName = 'table1'
    rootInstance = globals()[rootName]
    modelName = 'table2'
    nextModleName = 'table3'
    if nextModleName == '':
        nextModleName = modelName
    modelInstance = globals()[modelName]

    modelnameLst = ['table1', 'table2', 'table3', 'table4']

    #确定上一层model名并生成实例
    prevmodelname = ''
    for index in range(len(modelnameLst)):
        if modelnameLst[index] == modelName: 
            if index != 0:
                prevmodelname = modelnameLst[index - 1]
    # print('******',prevmodelname)
    rootName = prevmodelname
    rootInstance = globals()[rootName]

     #确定返回为什么
    goback = ''
    if prevmodelname == modelnameLst[0]:
        goback = '/'+rootFilePath+'/'+prevmodelname
    else:
        goback = '/'+rootFilePath+'/'+prevmodelname+'/' + str(rootInstance.objects.all()[0].id)

    
    # 如果是返回,用上一层的tableId肯定找不到bindkey,找到上一层instance的bind
    try:
        bindkey = rootInstance.objects.get(id = tableId)
    except:
        ins = modelInstance.objects.get(id = tableId)
        tableId = ins.bind.id
    try:
        bindkey = rootInstance.objects.get(id = tableId)
        
        objLst = modelInstance.objects.filter(bind = bindkey) 
        obj = objLst[0]
        cs = getmodelfield(rootFilePath, modelName,exclude)
        
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
                    'modelName':modelName,'goback': goback,
                    'nextLayout':'/'+rootFilePath+'/'+nextModleName})
    except:
        renderFile = 'renderTable1.html'  
        return render(request,renderFile,
                    {'headerAndWidth':[],
                    'totalData':[],'status':0,
                    'tableId':tableId,'tableName':'',
                    'modelName':modelName,'goback': goback,
                    'nextLayout':'#'})
 
                
@login_required(login_url="/acount/login/")
def table3_view(request,tableId):
    rootName = 'table2'
    rootInstance = globals()[rootName]
    modelName = 'table3'
    nextModleName = 'table4'
    if nextModleName == '':
        nextModleName = modelName
    modelInstance = globals()[modelName]

    modelnameLst = ['table1', 'table2', 'table3', 'table4']

    #确定上一层model名并生成实例
    prevmodelname = ''
    for index in range(len(modelnameLst)):
        if modelnameLst[index] == modelName: 
            if index != 0:
                prevmodelname = modelnameLst[index - 1]
    # print('******',prevmodelname)
    rootName = prevmodelname
    rootInstance = globals()[rootName]

     #确定返回为什么
    goback = ''
    if prevmodelname == modelnameLst[0]:
        goback = '/'+rootFilePath+'/'+prevmodelname
    else:
        goback = '/'+rootFilePath+'/'+prevmodelname+'/' + str(rootInstance.objects.all()[0].id)

    
    # 如果是返回,用上一层的tableId肯定找不到bindkey,找到上一层instance的bind
    try:
        bindkey = rootInstance.objects.get(id = tableId)
    except:
        ins = modelInstance.objects.get(id = tableId)
        tableId = ins.bind.id
    try:
        bindkey = rootInstance.objects.get(id = tableId)
        
        objLst = modelInstance.objects.filter(bind = bindkey) 
        obj = objLst[0]
        cs = getmodelfield(rootFilePath, modelName,exclude)
        
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
                    'modelName':modelName,'goback': goback,
                    'nextLayout':'/'+rootFilePath+'/'+nextModleName})
    except:
        renderFile = 'renderTable1.html'  
        return render(request,renderFile,
                    {'headerAndWidth':[],
                    'totalData':[],'status':0,
                    'tableId':tableId,'tableName':'',
                    'modelName':modelName,'goback': goback,
                    'nextLayout':'#'})
 
                
@login_required(login_url="/acount/login/")
def table4_view(request,tableId):
    rootName = 'table3'
    rootInstance = globals()[rootName]
    modelName = 'table4'
    nextModleName = ''
    if nextModleName == '':
        nextModleName = modelName
    modelInstance = globals()[modelName]

    modelnameLst = ['table1', 'table2', 'table3', 'table4']

    #确定上一层model名并生成实例
    prevmodelname = ''
    for index in range(len(modelnameLst)):
        if modelnameLst[index] == modelName: 
            if index != 0:
                prevmodelname = modelnameLst[index - 1]
    # print('******',prevmodelname)
    rootName = prevmodelname
    rootInstance = globals()[rootName]

     #确定返回为什么
    goback = ''
    if prevmodelname == modelnameLst[0]:
        goback = '/'+rootFilePath+'/'+prevmodelname
    else:
        goback = '/'+rootFilePath+'/'+prevmodelname+'/' + str(rootInstance.objects.all()[0].id)

    
    # 如果是返回,用上一层的tableId肯定找不到bindkey,找到上一层instance的bind
    try:
        bindkey = rootInstance.objects.get(id = tableId)
    except:
        ins = modelInstance.objects.get(id = tableId)
        tableId = ins.bind.id
    try:
        bindkey = rootInstance.objects.get(id = tableId)
        
        objLst = modelInstance.objects.filter(bind = bindkey) 
        obj = objLst[0]
        cs = getmodelfield(rootFilePath, modelName,exclude)
        
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
                    'modelName':modelName,'goback': goback,
                    'nextLayout':'/'+rootFilePath+'/'+nextModleName})
    except:
        renderFile = 'renderTable1.html'  
        return render(request,renderFile,
                    {'headerAndWidth':[],
                    'totalData':[],'status':0,
                    'tableId':tableId,'tableName':'',
                    'modelName':modelName,'goback': goback,
                    'nextLayout':'#'})
 
                
@login_required(login_url="/login/")
def addSubTable_view(request,tableId,tableModel):
    
    path = request.path
    modelName = path.split('/')[-1]
    formName = modelName +'_Form'
    # print(formName)
    # print(globals().keys())
    form = globals()[formName]
    model = globals()[modelName]
    modelnameLst = ['table1', 'table2', 'table3', 'table4']
    prevmodelname = ''
    for index in range(len(modelnameLst)):
        if modelnameLst[index] == modelName: 
            if index != 0:
                prevmodelname = modelnameLst[index - 1]
    
    # print(tableId)
    if request.method == 'POST':
        form = form(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            if tableId == '0':# 如果tableId等于0意味着根表，没有foreign key
                pass
            else:
                # instance.bind = model.objects.get(id = tableId)
                bindTable = prevmodelname
                bindModel = globals()[bindTable]
                instance.bind = bindModel.objects.get(id = tableId)
                
            instance.save()
            
            rd = tableModel[0].lower() + tableModel[1:]
            if tableId == '0':
                return redirect('/testapp/'+rd+'/')
            return redirect('/testapp/'+rd+'/'+tableId)
    else:

        path = request.path
        modelName = path.split('/')[-1]
        formName = modelName +'_Form'
        form = globals()[formName]
        title = '添加厂区'
        rd = tableModel[0].lower() + tableModel[1:]
        goback = ''
        print(tableId)
        if tableId == '0':
            goback = '/testapp/'+rd
            print('yes')
        else:
            goback = '/testapp/'+rd+'/'+tableId
            print('no')
        print(goback)
        
        print('tableModel is',tableModel)
       

    return render(request,'form.html',{'form':form,
    'tableName':title,'goback':goback})

def updateRow_view(request,modelName,rowId,tableId):
    modelInstance = globals()[modelName]
    obj = modelInstance.objects.get(id = rowId)
    formName = modelName +'_Form'
    form = globals()[formName]
    modelnameLst = ['table1', 'table2', 'table3', 'table4']
    if request.method == 'POST':
        form = form(request.POST,instance = obj)
        if form.is_valid():
            form.save()
            if modelName == modelnameLst[0]:
                 return redirect("/"+rootFilePath+"/"+modelName+"/")
            return redirect("/"+rootFilePath+"/"+modelName+"/"+tableId)

    form = form(instance = obj)
    title = '修改表单'
    action = '/'+rootFilePath+'/updateRow/'+modelName+'/'+rowId+'/'+tableId
    goback = '/'+rootFilePath+'/'+modelName+'/'+tableId
    return render(request,'form.html',
    {'form':form,'tableName':title,
    'tableId':tableId,'action':action,'goback':goback})



def deleteRow_view(request,modelName,rowId,tableId):
    modelInstance = globals()[modelName]
    
    modelnameLst = ['table1', 'table2', 'table3']

    obj = modelInstance.objects.get(id = rowId)

    obj.delete()
    #先删除在查找

    
    if modelName == modelnameLst[0]:
        goback = '/'+rootFilePath+'/'+modelName
    else:
        
        goback = '/'+rootFilePath+'/'+modelName+'/' + tableId

    print(goback)
       
    return redirect(goback)


