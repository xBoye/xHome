# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-31 06:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('text_mining', '0007_delete_inames'),
    ]

    operations = [
        migrations.CreateModel(
            name='Names',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='名字')),
                ('alias', models.CharField(max_length=20, null=True, verbose_name='别名')),
                ('textbook', models.CharField(max_length=50, verbose_name='文本')),
                ('note', models.TextField(null=True, verbose_name='备注')),
            ],
        ),
        migrations.RemoveField(
            model_name='results',
            name='item',
        ),
        migrations.RemoveField(
            model_name='words',
            name='isfrom',
        ),
        migrations.AddField(
            model_name='results',
            name='textbook',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='words',
            name='textbook',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
