from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
import matplotlib
matplotlib.use('Agg')#没有这个会有main loop error
import matplotlib.pyplot as plt
from .tools import *
from .models import *
from .forms import *
import os
# 'status2' 代表分析
def analyze_view(request,tableId):
    bindkey = LevelFour.objects.get(id = tableId)
    # try:
    bindkey = LevelFour.objects.get(id = tableId)
    #一般情況一個表會有很多行所以要用filter,用get會報錯
    #header只用第一行的數據就可以得到,包括轉verbose_name的
    objLst = LevelFive.objects.filter(bind = bindkey) 
    obj = objLst[0]
    cs = getmodelfield('app', 'LevelFive',exclude)
    # cs look like {'id': 'id', '月份': '月份', '用水量': '用水量(m3)', '金额1': '金额(元)', '用电量': '用水量(kw.h)', '金额2': '金额(元)', 'bind': 'bind'}
    header = getHeader(obj.__dict__,start = 1, end = (len(obj.__dict__) - 1),cs = cs)
    header1 = getHeader(obj.__dict__,start = 2, end = (len(obj.__dict__) - 3),cs = None)
    
    dataLst = []
    for obj in objLst:
        tem = []
        tem.append(obj.月份)
        tem.append(obj.用水量)
        tem.append(obj.用水量计划)
        dataLst.append(tem)
    # header1 是models原生attribute名，header是轉換過的verbose_name
    #render style
    dataLst1 = []
    for obj in objLst:
        tem = []
        tem.append(obj.月份)
        tem.append(obj.用电量)
        tem.append(obj.用电量计划)
        dataLst1.append(tem)
    width = [100,100,100,100,100,100]
    renderFile = 'renderAnalyze.html' 
    headerAndWidth = zip(header,width)
    totalData = loadData(objLst, header1)
    
    waterCompare = []
    energyCompare = []
    for i in totalData:
        id = i['id']
        lst = LevelFive.objects.filter(id = id)
        waterCompare.append(getColoumnsCompare(lst,'用水量','用水量计划'))
        energyCompare.append(getColoumnsCompare(lst,'用电量','用电量计划'))
    t = zip(dataLst,waterCompare)
    t1 = zip(dataLst1,energyCompare)
    print('dfsasdfsafs',t1)
    # dataLst = [[2,3],[5,6],[8,9]],compare[[1,1,1]]
    # for i,j in zip(datalst,compare):
    #    for q in i:
    #       print(q)
    #    for w in i:
    #       print(w)
    #    2,3,1;5,6,1;8,9,1  

    tableName =  bindkey.title + '消耗分析'
    waterCompareName = bindkey.title + '用水消耗分析'
    energyCompareName =  bindkey.title + '用电消耗分析'
    # print(waterCompare)
    # print(energyCompare)
    # waterAnalyze = zip(dataLst,waterCompare)
    watetAnalyzeHeader = zip(['月份','用水量(m3)','计划量(m3)','节约-/超出+'],width)
    energyAnalyzeHeader = zip(['月份','用电量(kwh)','计划量(kwh)','节约-/超出+'],width)

    if os.path.exists("./mystatic/image/watercost.jpg"):
        os.remove('./mystatic/image/watercost.jpg')
    monthlst = []
    waterCostlst = []
    energyCostlst = []
    for obj in objLst:
        monthlst.append(obj.月份)
        waterCostlst.append(obj.用水量)
        energyCostlst.append(obj.用电量)
    plt.rcParams['font.family']=['STFangsong']
    xpoints = monthlst
    ypoints = waterCostlst
    plt.title('月度用水量')
    plt.xlabel("月份")
    plt.ylabel('用水量')
    plt.plot(xpoints,ypoints)
    plt.savefig('./mystatic/image/watercost.jpg')
    plt.cla()

    if os.path.exists("./mystatic/image/energycost.jpg"):
        os.remove('./mystatic/image/energycost.jpg')
    plt.rcParams['font.family']=['STFangsong']
    xpoints = monthlst
    ypoints = energyCostlst
    plt.title('月度用电量')
    plt.xlabel("月份")
    plt.ylabel('用电量')
    plt.plot(xpoints,ypoints)
    plt.savefig('./mystatic/image/energycost.jpg')
    plt.cla()
    
    # with open('./mystatic/file.txt','w',encoding='utf-8') as f:
    #     f.write('aaaa')

    return render(request,renderFile,
                {'headerAndWidth':watetAnalyzeHeader,
                'headerAndWidth1':energyAnalyzeHeader,
                'totalData':t,'totalData1':t1,
                'status':2,'tableId':tableId,'tableName':tableName,
                
                'waterCompareName':waterCompareName,'energyCompareName':energyCompareName,
                'goback':'/app/levelFive/1'})
    
    return HttpResponse(1)
    # except :
    #     renderFile = 'renderAnalyze.html'  
    #     return render(request,renderFile,
    #                 {'headerAndWidth':[],
    #                 'planData':[],'status':2,
    #                 'tableId':tableId,'tableName':'EMPTY'}) 