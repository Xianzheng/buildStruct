# Generated by Django 3.2.14 on 2023-01-16 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0003_table4'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table1',
            name='title',
            field=models.CharField(default='', max_length=20, verbose_name='用水量'),
        ),
    ]
