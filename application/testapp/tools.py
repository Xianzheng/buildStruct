import datetime
from django.apps import apps
def loadData(objLst,header:list) -> list:
    #遍历所有表的所有信息填入total list中
    #最后total会变成比如[[],[],[]]

    total = []
    # print('header is',header)
    for obj in objLst:
        # temp装的的是每行的内容
        dic = {}
        temp = []
        # idlst 给每行的内容绑上相同的id
        id = obj.id
        for i in header:
            # getattr(obj,i)可以得到class instance 里 属性i的值
            # 這裏傳入的是modle的原生attribute,不是轉換過的verbose
            n = getattr(obj, i)
            #如果这是datetime.datetime的实例，只取日期显示
            if isinstance(n, datetime.datetime):
                n = n.date
            temp.append(n)
        dic['id'] = id
        dic['data'] = temp

        total.append(dic)
    # total look like [{'id':1,data:[...]},{'id':2,data:[...]}]
    return total

def getmodelfield(appname,modelname,exclude):
    """
    获取model的verbose_name和name的字段
    """
    modelobj = apps.get_model(appname, modelname)
    filed = modelobj._meta.fields
    # print(filed)
    fielddic = {}
 
    params = [f for f in filed if f.name not in exclude]
 
    for i in params:
        fielddic[i.name] = i.verbose_name
    # fielddic 
    # looks like {'id': 'id', '月份': '月份', '用水量': '用水量(m3)', '金额1': '金额(元)', '用电量': '用水量(kw.h)', '金额2': '金额(元)', 'bind': 'bind'}
    # dic's key is model attribute, value is verbose
    return fielddic

def getHeader(obj:dict,**vardict) -> list:
    '''
    param: dict
    result: 得到字典的所有key的list从字典從第幾位到開始到第幾位結束
    '''
    # 如果沒有沒有CS指明，代表取表的所有value
    if vardict['cs'] is None:
        lst = []
        #得到obj的所有key
        for i in obj:
            lst.append(i)
        #返回规定位数的key的
        # print('end is',vardict['end'])
        return lst[vardict['start']:vardict['end']]
    else:
        # 如果沒有有CS指明，想要得到header，通常是verbose
        cs = vardict['cs']
        lst = []
        #得到obj的所有key
        for i in obj:
            # print('i is',i)
            if i not in cs:
                # print('none is ',i)
                pass
            else:
                # print('in here i ',i)
                lst.append(cs[i])
        #返回规定位数的key的
        # print('end is',vardict['end'])
        return lst[vardict['start']:vardict['end']]

def getColoumnsCompare(lst,attr1,attr2):
    lst1 = []
    lst2 = []
    for obj in lst:
        lst1.append(getattr(obj,attr1))
        lst2.append(getattr(obj,attr2))
    
    lst3 = []
    for item1,item2 in zip(lst1,lst2):
        item = item2 - item1
        lst3.append(item)
    return lst3

exclude = ['username','email','is_staff','last_login','password','last_name','date_joined','is_active','is_superuser']