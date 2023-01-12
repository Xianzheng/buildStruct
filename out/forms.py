from .models import *
from django import forms

class table1_Form(forms.ModelForm):
    class Meta:
        model = table1

        fields = "__all__"

        exclude = ['id','bind']


        
            
class table2_Form(forms.ModelForm):
    class Meta:
        model = table2

        fields = "__all__"

        exclude = ['id','bind']


        
            
class table3_Form(forms.ModelForm):
    class Meta:
        model = table3

        fields = "__all__"

        exclude = ['id','bind']


        
            