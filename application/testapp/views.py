
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
    obj = modelInstance.objects.get(id = 1)
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

                
@login_required(login_url="/acount/login/")
def table2_view(request,tableId):
    rootName = 'table1'
    rootInstance = globals()[rootName]
    modelName = 'table2'
    nextModleName = ''
    if nextModleName == '':
        nextModleName = modelName
    modelInstance = globals()[modelName]
    bindkey = rootInstance.objects.get(id = tableId)
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
                    'modelName':modelName,'goback':'/app/'+rootName,
                    'nextLayout':'/'+rootFilePath+'/'+nextModleName})
    except:
        renderFile = 'renderTable1.html'  
        return render(request,renderFile,
                    {'headerAndWidth':[],
                    'totalData':[],'status':0,
                    'tableId':tableId,'tableName':'',
                    'modelName':'/'+rootFilePath+'/'+nextModleName,'goback':'rootName',
                    'nextLayout':'#'})

@login_required(login_url="/login/")
def addSubTable_view(request,tableId,tableModel):
    print('tableId is ',tableId)
    print('tableModel is',tableModel,type(tableModel))
    path = request.path
    modelName = path.split('/')[-1]
    formName = modelName +'_Form'
    print(formName)
    print(globals().keys())
    form = globals()[formName]
    model = globals()[modelName]
    bindTable = 'table1'
    bindModel = globals()[bindTable]
    print(tableId)
    if request.method == 'POST':
        form = form(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            if tableId == '0':# 如果tableId等于0意味着根表，没有foreign key
                pass
            else:
                # instance.bind = model.objects.get(id = tableId)
                
                instance.bind = bindModel.objects.get(id = tableId)
                
            instance.save()
            
            rd = tableModel[0].lower() + tableModel[1:]
            return redirect('/testapp/'+rd+'/'+tableId)
    else:

        path = request.path
        modelName = path.split('/')[-1]
        formName = modelName +'_Form'
        form = globals()[formName]
        title = '添加厂区'
        rd = tableModel[0].lower() + tableModel[1:]
        print(rd)
        goback = '/testapp/'+rd+'/'+tableId

    return render(request,'form.html',{'form':form,
    'tableName':title,'goback':goback})
 
                