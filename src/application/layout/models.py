from django.db import models

# Create your models here.
class LevelOne(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    year = models.IntegerField()
    title = models.CharField(max_length=50)

class LevelTwo(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=50)
    bind = models.ForeignKey(LevelOne, default=None, on_delete=models.CASCADE)

class LevelThree(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=50)
    bind = models.ForeignKey(LevelTwo, default=None, on_delete=models.CASCADE)




