# Generated by Django 3.2.14 on 2023-01-17 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table1',
            name='year',
            field=models.DateTimeField(verbose_name='更改日期'),
        ),
    ]
