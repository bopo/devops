# Generated by Django 3.1 on 2020-08-28 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hostgroup',
            options={'verbose_name': '主机管理', 'verbose_name_plural': '主机管理'},
        ),
    ]