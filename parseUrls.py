'''
打开或者穿件./out/url.py文件写入关于headers,load library
还包含了urlpatterns = [
'''
def writeUrlLoad():
    with open('./out/urls.py','w') as f:
        f.write('from django.urls import path ,include\n')
        f.write('from .views import *\n')
        f.write('urlpabetterns = [\n')
        f.close()
'''
打开./draw/drawModels.txt读取所有的model名
存入modelname链表
然后打开或者创建./out/urls.py'写入url信息根据model名
比如model名是tabel1,写入path('table1/',table1_view)到urls.py文件
'''
def writeUrlBody():
    modelnameLst = []
    with open('./draw/drawModels.txt','r') as f:
    
        lst = f.readlines()

        for index in range(len(lst)):
            parselst = lst[index].split(':')
            name = parselst[0]#得到class的名字
            body = parselst[1].replace('\n','')
            modelnameLst.append(name)

        f.close()
    #print(modelnameLst)
    with open('./out/urls.py','a') as f:
        for i in modelnameLst:
            f.write("    path('{}/',{}),\n".format(i,i+'_view'))
        f.write(']\n')
        f.close()
'''
运行function
'''
writeUrlLoad()
writeUrlBody()