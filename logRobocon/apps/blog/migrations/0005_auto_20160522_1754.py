# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-22 09:54
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blogpost_loggeneral'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='logContent',
            field=ckeditor.fields.RichTextField(verbose_name='日志正文'),
        ),
    ]