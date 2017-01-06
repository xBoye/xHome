# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-05 13:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Yi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gname', models.CharField(max_length=8, verbose_name='卦名')),
                ('gci', models.TextField(verbose_name='卦辞')),
                ('xci', models.TextField(verbose_name='象辞')),
                ('tci', models.TextField(verbose_name='彖辞')),
                ('y1', models.CharField(max_length=50, verbose_name='初爻')),
                ('x1', models.CharField(max_length=50, verbose_name='初爻小象')),
                ('y2', models.CharField(max_length=50, verbose_name='二爻')),
                ('x2', models.CharField(max_length=50, verbose_name='二爻小象')),
                ('y3', models.CharField(max_length=50, verbose_name='三爻')),
                ('x3', models.CharField(max_length=50, verbose_name='三爻小象')),
                ('y4', models.CharField(max_length=50, verbose_name='四爻')),
                ('x4', models.CharField(max_length=50, verbose_name='四爻小象')),
                ('y5', models.CharField(max_length=50, verbose_name='五爻')),
                ('x5', models.CharField(max_length=50, verbose_name='五爻小象')),
                ('y6', models.CharField(max_length=50, verbose_name='上爻')),
                ('x6', models.CharField(max_length=50, verbose_name='上爻小象')),
                ('yy', models.CharField(max_length=50, null=True, verbose_name='用爻')),
                ('xx', models.CharField(max_length=50, null=True, verbose_name='用爻小象')),
                ('wenyan', models.TextField(blank=True, null=True, verbose_name='文言')),
                ('gbin', models.CharField(max_length=6, verbose_name='二进制卦序')),
            ],
            options={
                'verbose_name_plural': 'yis',
            },
        ),
        migrations.CreateModel(
            name='Yilin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jname', models.CharField(max_length=10, verbose_name='易林卦名')),
                ('jci', models.TextField(blank=True, null=True, verbose_name='易林卦辞')),
                ('yi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yi.Yi')),
            ],
            options={
                'verbose_name_plural': 'yilins',
            },
        ),
    ]