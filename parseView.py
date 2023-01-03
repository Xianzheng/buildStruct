def writeViewLoad():
    with open('./out/views.py','w') as f:
        string = """
from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from .tools import getmodelfield, loadData, getHeader
from .models import *
from .forms import *
import sys
exclude = ['username','email','is_staff','last_login','password','last_name','date_joined','is_active','is_superuser']
        """
        f.write(string)

def writeViewBody():
    modelnameLst = []
    bodypartLst = []
    with open('./draw/drawModels.txt','r') as f:
    
        lst = f.readlines()

        for index in range(len(lst)):
            parselst = lst[index].split(':')
            name = parselst[0]#得到class的名字
            body = parselst[1].replace('\n','')
            modelnameLst.append(name)
            bodypartLst.append(body)
        f.close()
    with open('./out/views.py','a',encoding = 'utf-8') as f:
        
        for index in range(len(modelnameLst)):
            if index == 0:
                modelName = modelnameLst[index]
                print(modelName)
                # model = globals()[modelName]
                string = """
@login_required(login_url="/acount/login/")
def {}_view(request):
    modelName = {}
    modelInstance = globals()[modelName]
    #得到表的第一个obj
    obj = modelInstance.objects.get(id = 1)
    #传入obj的字典格式obj.__dict__函数getheader得到表的第二项到最后一项
    cs = getmodelfield('app', modelName,exclude)
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
                'goback':'/logout/','nextLayout':'table2'})\n
                """
                string = string.replace('{}',modelName)
                f.write(string)
            else:
                modelName = modelnameLst[index]
                bodypart = bodypartLst[index]
                print(modelName)
                rootName = bodypart.split(',')[-1].split()[0]#得到foreign key model的名字
                print(rootName)
                string = '''
@login_required(login_url="/acount/login/")
def {1}_view(request,tableId):
    rootName = {2}
    rootInstance = globals()[rootName]
    modelName = {1}
    modelInstance = globals()[modelName]
    bindkey = rootInstance.objects.get(id = tableId)
    try:
        bindkey = rootInstance.objects.get(id = tableId)
        
        objLst = modelInstance.objects.filter(bind = bindkey) 
        obj = objLst[0]
        cs = getmodelfield('app', modelName,exclude)
        
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
                    'nextLayout':'#'})
    except:
        renderFile = 'renderTable1.html'  
        return render(request,renderFile,
                    {'headerAndWidth':[],
                    'totalData':[],'status':0,
                    'tableId':tableId,'tableName':'',
                    'modelName':modelName,'goback':'rootName',
                    'nextLayout':'#'})\n 
                '''
                string = string.replace('{1}',modelName).replace('{2}',rootName)
                f.write(string)
        

writeViewLoad()
writeViewBody()

