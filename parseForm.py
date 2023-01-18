def getAttriNameForDateField(string):
    '''
    找出包含 date string 的attribute名字，
    string example,
    id auto,title string vb-用水量 max-100 ,cost int vb-消耗,year date vb-更新日期
    '''
    lst = string.split(',')
    name = ''
    for index in range(len(lst)):
        if 'date' in lst[index]:
            
            return lst[index].split()[0]
    return None
        

def writeFormLoad():
    with open('./out/forms.py','w',encoding='utf-8') as f:
        f.write('from .models import *\n')
        f.write('from django import forms\n')
        f.close()

def writeFormBody():
    modelnameLst = []
    bodypartLst = []
    containDate = []
    with open('./draw/drawModels.txt','r',encoding='utf-8') as f:
    
        lst = f.readlines()

        for index in range(len(lst)):
            parselst = lst[index].split(':')
            # print(parselst)
            name = parselst[0]#得到class的名字
            body = parselst[1].replace('\n','')
            
            modelnameLst.append(name)
            bodypartLst.append(body)
        f.close()

    with open('./out/forms.py','a',encoding='utf-8') as f:
        for index in range(len(modelnameLst)):
            string = """
class {}_Form(forms.ModelForm):
    class Meta:
        model = {}

        fields = "__all__"

        exclude = ['id','bind']\n

        
            """

            string = string.replace('{}',modelnameLst[index])
            if getAttriNameForDateField(bodypartLst[index]):
                attriName = getAttriNameForDateField(bodypartLst[index])
                print(attriName)
                addString = """
        widgets = {
                    {}: forms.widgets.DateInput(attrs={'type':'date'}),
                }
                """
                addString = addString.replace('{}','\''+attriName+'\'')
                string = string + addString
            
            f.write(string)
writeFormLoad()
writeFormBody()