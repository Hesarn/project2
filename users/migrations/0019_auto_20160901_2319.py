# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-01 23:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_auto_20160901_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='picture',
            field=models.ImageField(default='img/user.png', upload_to='photo/'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='profilePicture',
            field=models.ImageField(default='img/user.png', upload_to='photo/'),
        ),
    ]
