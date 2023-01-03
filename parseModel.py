def writeAttribute(itemname,itemtype):#*agr,**kagr
    # print(itemtype)
    string = ''

    if itemtype == 'auto':     
        string = itemname+ \
            ' = '+"models.AutoField(primary_key=True,auto_created=True)"
            
    if itemtype == 'string':     
        string = '    '+\
            itemname+' = '+"models.CharField(max_length=20,default = '')"

    if itemtype == 'int':     
        string = '    '+itemname+' = '+"models.IntegerField(default = 0)"

    if itemtype == 'foreignKey':
        string = '    '+'bind'+' = '+\
            "models.ForeignKey({},default=None,on_delete=models.CASCADE)".format(itemname)
            
    with open('./out/models.py','a',encoding='utf-8') as f1:
        # print(string)
        f1.write(string)
        f1.write('\n')
        # f1.close()

with open('./out/models.py','w') as f1:
    f1.write('from django.db import models')
    f1.close()

with open('./out/admin.py','w') as f1:
    f1.write('from django.contrib import admin\n')
    f1.write('from .models import *\n')
    f1.close()

with open('./draw/drawModels.txt','r') as f:
    
    lst = f.readlines()

    for index in range(len(lst)):
        parselst = lst[index].split(':')
        name = parselst[0]#得到class的名字
        body = parselst[1].replace('\n','')
        #print(body)#得到id auto,title string,year date之类的
        bodylst = body.split(',')
       #print(bodylst)得到['id auto', 'title string', 'year date\n']
         #attribute type
        with open('./out/models.py','a') as f1:
            string = '''
class {}:
    '''.format(name+"(models.Model)").replace('/t','')
            f1.write(string)
            # f1.close()
        for item in bodylst:
            itemlst = item.split()
            itemname = itemlst[0] #attribute name
            itemtype = itemlst[1]
            
            writeAttribute(itemname,itemtype)
        with open('./out/admin.py','a') as f2:
            f2.write('admin.site.register({})\n'.format(name))

        


        
