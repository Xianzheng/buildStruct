# Generated by Django 3.2.14 on 2023-01-10 22:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='table3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=20)),
                ('age', models.CharField(default='', max_length=20)),
                ('bind', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='testapp.table2')),
            ],
        ),
    ]
