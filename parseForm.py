def writeFormLoad():
    with open('./out/forms.py','w',encoding='utf-8') as f:
        f.write('from .models import *\n')
        f.write('from django import forms\n')
        f.close()

def writeFormBody():
    modelnameLst = []
    bodypartLst = []
    with open('./draw/drawModels.txt','r',encoding='utf-8') as f:
    
        lst = f.readlines()

        for index in range(len(lst)):
            parselst = lst[index].split(':')
            name = parselst[0]#得到class的名字
            body = parselst[1].replace('\n','')
            modelnameLst.append(name)
            bodypartLst.append(body)
        f.close()

    with open('./out/forms.py','a',encoding='utf-8') as f:
        for i in modelnameLst:
            string = """
class {}_Form(forms.ModelForm):
    class Meta:
        model = {}

        fields = "__all__"

        exclude = ['id','bind']\n

        
            """

            string = string.replace('{}',i)
            f.write(string)
writeFormLoad()
writeFormBody()