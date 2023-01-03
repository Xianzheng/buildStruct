from .models import *
from django import forms

class 消耗表(forms.ModelForm):
    class Meta:
        model = 消耗

        fields = "__all__"

        exclude = ['id','bind']

        lable = {
            '用水量':'用水量(m3)',
            '金额1':'金额（元）',
            '用电量':'用电量(m3)',
            '金额2':'金额（元）',
        }

class LevelOne_Form(forms.ModelForm):
    class Meta:
        model = LevelOne

        fields = "__all__"

        exclude = ['id','bind']

        lable = {
            'title':'厂区名',
            'year':'年度',
        }

class LevelTwo_Form(forms.ModelForm):
    class Meta:
        model = LevelTwo

        fields = "__all__"

        exclude = ['id','bind']

        lable = {
            'title':'分厂名',
        }

class LevelThree_Form(forms.ModelForm):
    class Meta:
        model = LevelThree

        fields = "__all__"

        exclude = ['id','bind']

        lable = {
            'title':'单位名',
        }

class LevelFour_Form(forms.ModelForm):
    class Meta:
        model = LevelFour

        fields = "__all__"

        exclude = ['id','bind']

        lable = {
            'title':'单位名',
        }

class LevelFive_Form(forms.ModelForm):
    class Meta:
        model = LevelFive

        fields = "__all__"

        exclude = ['id','bind']

        lable = {
            '用水量':'用水量(m3)',
            '金额1':'金额（元）',
            '用电量':'用电量(m3)',
            '金额2':'金额（元）',
        }
    