def getKeywordIndex(key,lst):
    '''
    得到包含keyword关键字在的index
    '''
    for index in range(len(lst)):
        if key in lst[index]:
            return index
    return None

def getKeywordContent(key,remainder):
    '''
    因为有vb的内容一般长'vb-名字'这样，
    所以取vb-后面的内容为KeywordContent
    '''
    if getKeywordIndex('vb',remainder) != None:
        vbIndex = getKeywordIndex('vb',remainder)
        vbContent = remainder[vbIndex].split('-')[-1]
        return vbContent
    return None

def addField(key,lst,string):
    '''
    拿到Keyword之后再对attibute中增加Field verbose_name 是什么
    '''
    if lst:
        vbContent = getKeywordContent(key,lst)
        if vbContent:
            print(vbContent)
            return string[:-1] + 'verbose_name = '+'\''+vbContent+'\')'
            
    return string

def writeAttribute(**attri):#*agr,**kagr
    # print(itemtype)
    remainder = attri['lst'] #除了attribute name, 和 type剩余的  都放在一个lst里后续添加,rint
    
    string = ''

    if attri['type'] == 'auto':     
        string = attri['name']+ \
            ' = '+"models.AutoField(primary_key=True,auto_created=True,)"
        
    if attri['type'] == 'string':     
        string = '    '+\
            attri['name']+' = '+"models.CharField(max_length=20,default = '',)"
        string = addField('vb',remainder,string)

    if attri['type'] == 'int':     
        string = '    '+attri['name']+' = '+"models.IntegerField(default = 0,)"
        string = addField('vb',remainder,string)

    if attri['type'] == 'date':
        string = '    '+ attri['name']+'= models.DateTimeField()'
        string = addField('vb',remainder,string)

    if itemtype == 'foreignKey':
        string = '    '+'bind'+' = '+\
            "models.ForeignKey({},default=None,on_delete=models.CASCADE)".format(itemname)

    
    
            
    with open('./out/models.py','a',encoding='utf-8') as f1:
        # print(string)
        f1.write(string)
        f1.write('\n')
        f1.close()
        

with open('./out/models.py','w',encoding='utf-8') as f1:
    f1.write('from django.db import models\n')
    f1.write('import datetime\n')
    f1.close()

with open('./out/admin.py','w',encoding='utf-8') as f1:
    f1.write('from django.contrib import admin\n')
    f1.write('from .models import *\n')
    f1.close()

with open('./draw/drawModels.txt','r',encoding = 'utf-8') as f:
    
    lst = f.readlines()

    for index in range(len(lst)):
        parselst = lst[index].split(':')
        name = parselst[0]#得到class的名字
        body = parselst[1].replace('\n','')
        #print(body)#得到id auto,title string,year date之类的
        bodylst = body.split(',')
        # print(bodylst)
       #print(bodylst)得到['id auto', 'title string', 'year date\n']
         #attribute type
        with open('./out/models.py','a') as f1:
            string = '''
class {}:
    '''.format(name+"(models.Model)").replace('/t','')
            f1.write(string)
            f1.close()
        for item in bodylst:
            itemlst = item.split()
            itemname = itemlst[0] #attribute name
            itemtype = itemlst[1]
            itemElse = itemlst[2:]
            
            writeAttribute(name = itemname, type = itemtype, lst  = itemElse )
        with open('./out/admin.py','a',encoding='utf-8') as f2:
            
            f2.write('admin.site.register({})\n'.format(name))
            f2.close()

        


        
