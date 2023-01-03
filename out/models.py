from django.db import models
class table1(models.Model):
    id = models.AutoField(primary_key=True,auto_created=True)
    title = models.CharField(max_length=20,default = '')


class table2(models.Model):
    id = models.AutoField(primary_key=True,auto_created=True)
    title = models.CharField(max_length=20,default = '')
    bind = models.ForeignKey(table1,default=None,on_delete=models.CASCADE)
