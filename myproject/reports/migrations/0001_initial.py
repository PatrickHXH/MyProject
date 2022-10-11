# Generated by Django 4.0.4 on 2022-10-11 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailManage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50, verbose_name='邮箱')),
                ('code', models.CharField(max_length=50, verbose_name='邮箱授权码')),
                ('server', models.CharField(max_length=50, verbose_name='服务器地址')),
                ('is_delete', models.IntegerField(default=0, verbose_name='删除')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
        ),
        migrations.CreateModel(
            name='SearchReportLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=50, null=True, verbose_name='测试报告名称')),
                ('sender', models.CharField(max_length=50, null=True, verbose_name='发送人')),
                ('receive', models.CharField(max_length=50, null=True, verbose_name='接收人')),
                ('text', models.TextField(null=True, verbose_name='正文')),
                ('source', models.CharField(max_length=50, null=True, verbose_name='来源')),
                ('email_id', models.IntegerField(null=True, verbose_name='邮件id')),
                ('report_time', models.DateTimeField(null=True, verbose_name='报告时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
        ),
    ]
