# Generated by Django 2.2 on 2019-12-04 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crawler', '0002_auto_20191205_0151'),
    ]

    operations = [
        migrations.DeleteModel(
            name='NewsType',
        ),
        migrations.RemoveField(
            model_name='news',
            name='author',
        ),
    ]
