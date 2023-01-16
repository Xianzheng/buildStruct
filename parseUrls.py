'''
打开或者穿件./out/url.py文件写入关于headers,load library
还包含了urlpatterns = [
'''
def writeUrlLoad():
    with open('./out/urls.py','w',encoding='utf-8') as f:
        f.write('from django.urls import path ,include\n')
        f.write('from .views import *\n')
        f.write('urlpatterns = [\n')
        f.close()
'''
打开./draw/drawModels.txt读取所有的model名
存入modelname链表
然后打开或者创建./out/urls.py'写入url信息根据model名
比如model名是tabel1,写入path('table1/',table1_view)到urls.py文件
'''
def writeUrlBody():
    modelnameLst = []
    with open('./draw/drawModels.txt','r',encoding='utf-8') as f:
    
        lst = f.readlines()

        for index in range(len(lst)):
            parselst = lst[index].split(':')
            name = parselst[0]#得到class的名字
            body = parselst[1].replace('\n','')
            modelnameLst.append(name)

        f.close()
    #print(modelnameLst)
    with open('./out/urls.py','a',encoding='utf-8') as f:
        for index in range(len(modelnameLst)):
            if index == 0:
                i = modelnameLst[index]
                f.write("    path('{}/',{}),\n".format(i,i+'_view'))
            else:
                i = modelnameLst[index]
                f.write("    path('{}/<tableId>',{}),\n".format(i,i+'_view'))
        f.write("    path('addSubTable/<tableId>/<tableModel>',addSubTable_view),\n")
        f.write("    path('updateRow/<modelName>/<rowId>/<tableId>',updateRow_view),\n")
        f.write("    path('deleteRow/<modelName>/<rowId>/<tableId>',deleteRow_view),\n")
        f.write(']\n')
        f.close()


'''
运行function
'''
writeUrlLoad()
writeUrlBody()