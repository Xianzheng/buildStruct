from django.db import models
# Create your models here.
class 厂区(models.Model):
    id = models.AutoField(primary_key=True,auto_created=True)
    年度 = models.CharField(max_length=10,default = '')
    厂区名 = models.CharField(max_length=10)
    def __str__(self) -> str:
        return self.厂区名

class 消耗(models.Model):
    id = models.AutoField(primary_key=True,auto_created=True)
    month_choose = (('1','一月份'),('2','二月份'),('3','三月份'),('4','四月份'),('5','五月份'),('6','六月份'),('7','七月份'),('8','八月份'),('9','九月份'),('10','十月份'),('11','十一月份'),('12','十二月份'))
    月份 = models.CharField(max_length = 10,choices = month_choose,)
    用水量 = models.DecimalField(max_digits=1000000,decimal_places=2,verbose_name='用水量(m3)')
    金额1 = models.DecimalField(default = 0.00, max_digits=1000000,decimal_places=2,verbose_name = '金额(元)')
    用电量= models.DecimalField(max_digits=1000000,decimal_places=2,verbose_name='用电量(kw.h)')
    金额2 = models.DecimalField(default = 0.00,max_digits=1000000,decimal_places=2,verbose_name = '金额(元)')
    用水量计划 = models.DecimalField(default = 0.00,max_digits=1000000,decimal_places=2,verbose_name='用水量计划(m3)')
    用电量计划= models.DecimalField(default = 0.00,max_digits=1000000,decimal_places=2,verbose_name='用电量计划(kw.h)')
    bind = models.ForeignKey(厂区,default=None,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.bind.厂区名 + '消耗'

class LevelOne(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    year = models.IntegerField(verbose_name='年度')
    title = models.CharField(max_length=50,verbose_name='厂区名')
    def __str__(self) -> str:
        return self.title

class LevelTwo(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=50, verbose_name='厂区名')
    bind = models.ForeignKey(LevelOne, default=None, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.title

class LevelThree(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=50, verbose_name='厂区名')
    bind = models.ForeignKey(LevelTwo, default=None, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.title

class LevelFour(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=50, verbose_name='厂区名')
    bind = models.ForeignKey(LevelThree, default=None, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.title

class LevelFive(models.Model):
    id = models.AutoField(primary_key=True,auto_created=True)
    month_choose = (('1','一月份'),('2','二月份'),('3','三月份'),('4','四月份'),('5','五月份'),('6','六月份'),('7','七月份'),('8','八月份'),('9','九月份'),('10','十月份'),('11','十一月份'),('12','十二月份'))
    月份 = models.CharField(max_length = 10,choices = month_choose,)
    用水量 = models.DecimalField(default = 0.00,max_digits=1000000,decimal_places=2,verbose_name='用水量(m3)')
    金额1 = models.DecimalField(default = 0.00, max_digits=1000000,decimal_places=2,verbose_name = '金额(元)')
    用电量= models.DecimalField(default = 0.00,max_digits=1000000,decimal_places=2,verbose_name='用电量(kw.h)')
    金额2 = models.DecimalField(default = 0.00,max_digits=1000000,decimal_places=2,verbose_name = '金额(元)')
    用水量计划 = models.DecimalField(default = 0.00,max_digits=1000000,decimal_places=2,verbose_name='用水量计划(m3)')
    用电量计划= models.DecimalField(default = 0.00,max_digits=1000000,decimal_places=2,verbose_name='用电量计划(kw.h)')
    bind = models.ForeignKey(LevelFour,default=None,on_delete=models.CASCADE)



